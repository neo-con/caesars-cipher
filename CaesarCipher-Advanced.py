class CaesarCipher:
    def __init__(self):
        self.key = self.key_req()

    def encrypt(self, message):
        result = ""
        for letter in message:
            num = ord(letter) + self.key
            result += chr(num)
        return result

    def decrypt(self, message):
        result = ""
        for letter in message:
            num = ord(letter) - self.key
            result += chr(num)
        return result

    def key_req(self):
        while True:
            key = input("Enter a key (1-555000): ")
            if key.isdigit():
                key = int(key)
                if 1 <= key <= 555000:
                    return key
                else:
                    print("Key must be in the range of 1-555000.")
            else:
                print("Key must be a number.")

def main():
    message = input("Enter a message: ")
    cipher = CaesarCipher()
    encrypted_message = cipher.encrypt(message)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", cipher.decrypt(encrypted_message))

if __name__ == "__main__":
    main()


