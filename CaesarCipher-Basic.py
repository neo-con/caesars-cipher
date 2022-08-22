#Caesar's Cipher
def encrypt(message, key):
    result = ""
    for letter in message:
        num = ord(letter) + key
        if letter.isalpha():
            if letter.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif letter.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            result += chr(num)
        else:
            result += letter
    return result

def decrypt(message, key):
    result = ""
    for letter in message:
        num = ord(letter) - key
        if letter.isalpha():
            if letter.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif letter.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            result += chr(num)
        else:
            result += letter
    return result


def key_req():
    key = input("Enter a key: ")
    if key.isdigit():
        key = int(key)
        if key in range(1,26):
            return key
        else:
            print("Key must be in range of 1-26")
            key_req()
    else:
        print("Key must be a number")
        key_req()


def main():
    message = input("Enter a message: ")
    key = key_req()
    print("Encrypted message: " + encrypt(message, key))
    print("Decrypted message: " + decrypt(encrypt(message, key), key))

main()