from dearpygui import core, simple
import des

def get_rk_rkb(left, right):
    rkb = []
    rk  = []
    for i in range(0, 16):
        # Shifting the bits by nth shifts by checking from shift table
        left = des.shift_left(left, shift_table[i])
        right = des.shift_left(right, shift_table[i])
        
        # Combination of left and right string
        combine_str = left + right
        
        # Compression of key from 56 to 48 bits 
        round_key = des.permute(combine_str, key_comp, 48)
    
        rkb.append(round_key)
        rk.append(des.bin2hex(round_key))

    return rk, rkb

def get_initial_values(key):
    key = des.hex2bin(key)
    key = des.permute(key, keyp, 56)
    left = key[0:28]
    right = key[28:56]
    return key, left, right

def check_inputs(key, text):
    if len(key) != 16 or len(text) != 16:
        return False
    return True

def decrypt(sender, data):
    core.configure_item("Cannot Decrypt with plaintext", show=False)
    core.configure_item("Input and Key must be 64 bits", show=False)
    cipher_text = str(core.get_value("Input"))
    if (core.get_value("RadioButton##widget") == 1):
        core.configure_item("Cannot Decrypt with plaintext", show=True)
        return
    # padding
    while len(cipher_text) < 16:
        cipher_text += "0"
    key = str(core.get_value("Key"))
    # selected plain text
    if (core.get_value("RadioButton##widget1") == 1):
        key = key.encode().hex()
    # padding
    while len(key) < 16:
        key += "0"
    if not check_inputs(key, cipher_text):
        core.configure_item("Input and Key must be 64 bits", show=True)
        return
    window_name = "Decryption"
    other_window_name = "Encryption"
    if core.does_item_exist(window_name):
        core.delete_item(window_name)
    if core.does_item_exist(other_window_name):
        core.delete_item(other_window_name)
    key, left, right = get_initial_values(key)
    rk, rkb = get_rk_rkb(left, right)
    rkb_rev = rkb[::-1]
    rk_rev = rk[::-1]
    perm_str, round_str, text = des.encrypt(cipher_text, rkb_rev, rk_rev)
    with simple.window(window_name, width=450, height=380, x_pos=251, y_pos=0):
        core.add_text(perm_str)
        core.add_text("Round #    Left     Right")
        for i in range(len(round_str)):
            core.add_text(round_str[i])
        core.add_text("Plain Text in hex (after final permuation): " + text)
        plaintext = bytes.fromhex(text.lower()).decode('utf-8', "replace")
        core.add_text("Plain Text in clear text (after final permuation): " + plaintext)

def encrypt(sender, data):
    pt = str(core.get_value("Input"))
    core.configure_item("Cannot Decrypt with plaintext", show=False)
    core.configure_item("Input and Key must be 64 bits", show=False)
    # selected plain text
    if (core.get_value("RadioButton##widget") == 1):
        pt = pt.encode().hex()
    # padding
    while len(pt) < 16:
        pt += "0"
    key = str(core.get_value("Key"))
    # selected plain text
    if (core.get_value("RadioButton##widget1") == 1):
        key = key.encode().hex()
    # padding
    while len(key) < 16:
        key += "0"
    if not check_inputs(key, pt):
        core.configure_item("Input and Key must be 64 bits", show=True)
        return
    window_name = "Encryption"
    other_window_name = "Decryption"
    if core.does_item_exist(window_name):
        core.delete_item(window_name)
    if core.does_item_exist(other_window_name):
        core.delete_item(other_window_name)
    key, left, right = get_initial_values(key)
    rk, rkb = get_rk_rkb(left, right)
    perm_str, round_str, cipher_text = des.encrypt(pt, rkb, rk)
    with simple.window(window_name, width=450, height=360, x_pos=251, y_pos=0):
        core.add_text(perm_str)
        core.add_text("Round #    Left     Right")
        for i in range(len(round_str)):
            core.add_text(round_str[i])
        core.add_text("Cipher Text (after final permuation): " + cipher_text)

with simple.window("ECB DES Learning Tool", width=230, height=200, x_pos=0, y_pos=0):
    core.add_radio_button("RadioButton##widget", items=["Hex", "Plaintext"], horizontal=True)
    core.add_input_text("Input", height=100)
    core.add_radio_button("RadioButton##widget1", items=["Hex", "Plaintext"], horizontal=True)
    core.add_input_text("Key")
    core.add_button("Decrypt", callback=decrypt)
    core.add_button("Encrypt", callback=encrypt)
    core.add_text("Input and Key must be 64 bits", color=[255, 0, 0, 255], show=False)
    core.add_text("Cannot Decrypt with plaintext", color=[255, 0, 0, 255], show=False)

# --parity bit drop table
keyp = [57, 49, 41, 33, 25, 17, 9, 
        1, 58, 50, 42, 34, 26, 18, 
        10, 2, 59, 51, 43, 35, 27, 
        19, 11, 3, 60, 52, 44, 36, 
        63, 55, 47, 39, 31, 23, 15, 
        7, 62, 54, 46, 38, 30, 22, 
        14, 6, 61, 53, 45, 37, 29, 
        21, 13, 5, 28, 20, 12, 4 ]

# Number of bit shifts 
shift_table = [1, 1, 2, 2, 
                2, 2, 2, 2, 
                1, 2, 2, 2, 
                2, 2, 2, 1 ]
  
# Key- Compression Table : Compression of key from 56 bits to 48 bits
key_comp = [14, 17, 11, 24, 1, 5, 
            3, 28, 15, 6, 21, 10, 
            23, 19, 12, 4, 26, 8, 
            16, 7, 27, 20, 13, 2, 
            41, 52, 31, 37, 47, 55, 
            30, 40, 51, 45, 33, 48, 
            44, 49, 39, 56, 34, 53, 
            46, 42, 50, 36, 29, 32 ]

core.set_main_window_size(750, 430)
core.start_dearpygui()
