#Ceasar's Cipher-Advanced.py
def encrypt(message, key):
    result = ""
    for letter in message:
        num = ord(letter) + key
        result += chr(num)
    return result

def decrypt(message, key):
    result = ""
    for letter in message:
        num = ord(letter) - key
        result += chr(num)
    return result


#The valid range for the chr() function is 0 through 1,114,111. However, we will use roughly half of that range.
def key_req():
    key = input("Enter a key: ")
    if key.isdigit():
        key = int(key)
        if key in range(1,555000):
            return key
        else:
            print("Key must be in range of 1-555000")
            key_req()
    else:
        print("Key must be a number")
        key_req()    



#Runs a while loop to continue asking for key if invalid.
def main():
    message = input("Enter a message: ")
    key = key_req()
    print("Encrypted message:", encrypt(message, key))
    print("Decrypted message:", decrypt(encrypt(message, key), key))

main()


