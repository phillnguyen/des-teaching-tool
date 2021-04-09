from dearpygui import core, simple
import des

def decrypt(sender, data):
    text_input = str(core.get_value("Input"))
    key = str(core.get_value("Key"))
    with simple.window("Decryption"):
        core.add_text(key)

def encrypt(sender, data):
    text_input = str(core.get_value("Input"))
    key = str(core.get_value("Key"))
    with simple.window("Encryption"):
        core.add_text(key)

with simple.window("DES Interactive Learning Tool", width=250, height=250, x_pos=0, y_pos=0):
    core.add_text("Hello world")
    core.add_radio_button("RadioButton##widget", items=["Plaintext", "Hex"])
    core.add_input_text("Input")
    core.add_radio_button("RadioButton##widget1", items=["Plaintext", "Hex"])
    core.add_input_text("Key")
    core.add_button("Decrypt", callback=decrypt)
    core.add_button("Encrypt", callback=encrypt)
    core.add_text(des.xor("1100", "0011"))

core.set_main_window_size(1500, 800)
core.start_dearpygui()
