# Caesars-Cipher

This repository includes two implementations of the Caesar Cipher: one basic and one advanced. The basic version encrypts only alphabetic characters, while the advanced version shifts all characters, including numbers, letters, spaces, and symbols.

## Caesars_Cipher-Basic.py

This program encrypts and decrypts messages using a Caesar Cipher technique. It takes a message and a key as input. The key must be a number between 1 and 25. The encryption and decryption only affect alphabetic characters; all other characters (like spaces and punctuation) are not altered.

**Features:**
- Encrypts and decrypts messages using a shift key that the user provides.
- Maintains non-alphabetic characters unchanged in the output.
- Prompts the user to enter a valid key if the provided key is out of the acceptable range.

**Example Usage:**

* Enter a message: My name is Neo.
* Enter a key: 12 
* Encrypted message: Yk zmyq ue Zqa.
* Decrypted message: My name is Neo.

## Caesars_Cipher-Advanced.py

This version of the Caesar Cipher shifts every character in the input message by a user-defined key, which can be any number from 1 to 555000. This includes letters, numbers, spaces, and symbols.

**Features:**
- Encrypts and decrypts any printable characters.
- Allows a very large range of shift values (up to 555000).
- Ensures that the user inputs a valid numeric key within the specified range.

**Example Usage:**

* Enter a message: My name is Neo.
* Enter a key: 250
* Encrypted message: ŇųĚŨśŧşĚţŭĚňşũĨ
* Decrypted message: My name is Neo.

## General Information

Both versions of the Caesar Cipher are implemented in Python. They use the `ord()` and `chr()` functions to convert characters to their corresponding ASCII values and back. The basic version adjusts the ASCII values based on whether characters are uppercase or lowercase to maintain proper alphabetic shifts. The advanced version shifts all characters indiscriminately by the specified key value.
