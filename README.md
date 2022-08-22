# Caesars_Cipher

Includes two files. One basic and the other advanced (which only means that we shift everything; numbers, letters, spaces, symbols, etc..)

## Caesars_Cipher-Basic.py

This program takes a message and a key as input and encrypts the message using the key. I use the ord() and chr() built-in functions to convert the letters to numbers and vice versa avoiding having to create a string of the alphabet. It just makes things easier. Because a lower case and capital case letter have different values, I have to check if the letter is upper or lower case and then add or subtract the key accordingly.

Because the basic only converts letters, I have to check if the letter is a letter or not. If it is not a letter, I just add it to the result string. This keeps spaces and punctuations in the encryption (perhaps something you wouldn't really want to do in a real encryption).

**Example:**

* Enter a message: My name is Neo.

* Enter a key: 12 

* Encrypted message: Yk zmyq ue Zqa.

* Decrypted message: My name is Neo.


## Caesars_Cipher-Advanced.py

This program takes a message and a key as input and encrypts the message using the key. I use the ord() and chr() built-in functions to convert the letters to numbers and vice versa avoiding having to create a string of the alphabet. In this case, we do not care to keep the values of the alphabet (A-Z) or (a-z) so we just shift everything.

**Example:**

* Enter a message: My name is Neo.

* Enter a key: 250

* Encrypted message: ŇųĚŨśŧşĚţŭĚňşũĨ

* Decrypted message: My name is Neo.
