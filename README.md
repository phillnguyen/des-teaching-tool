# ECB DES Teaching Tool
This is an interactive tool that decrypts and encrypts using Electronic Code Book Data Encryption Standard (ECB DES). It takes an online DES converter a step further by showing the bytes (in hex) in between each round. This project makes use of the DearPyGUI frontend framework for the UI and code from Geeks for Geeks: https://www.geeksforgeeks.org/data-encryption-standard-des-set-1/ for the DES algorithm. 

Github Link: https://github.com/phillnguyen/des-teaching-tool 

## How to run
1. Install python 3 from here: https://www.python.org/downloads/ 
2. While installing python 3, ensure that you use the installer to config you enviroment variables to enable the pip command
3. Install dependencies using `pip install <insert dependency name>`
4. Run using `python3 tool.py` or `python tool.py` inside the project directory.
## Known Dependencies 
These should be installed using `pip install <insert dependency name>` (Example: `pip install dearpygui`)
1. dearpygui 0.6.294
## Limitations
1. Can only do ECB DES
2. Inputs must be less than 128 bits (length 32 hex, length 16 plaintext). 64 < bits <= 128 bits will run DES twice. <= 64 bits will run once.
3. To get clear text outputs, hex is decoded in utf-8. Based on hex outputs, some characters may appear as '?' if the character cannot be decoded using utf-8
4. Key is not verified using parity bits.
5. Program assumes to user inputs plain text, cipher text, and key according to the selected radio button preceding the text input.