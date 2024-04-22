class CaesarCipher:
    def __init__(self, key=None):
        self.key = key if key is not None else self.key_req()

    def shift_char(self, c, key):
        if c.isalpha():
            start = ord('A') if c.isupper() else ord('a')
            offset = (ord(c) - start + key) % 26
            return chr(start + offset)
        return c

    def encrypt(self, message):
        return ''.join(self.shift_char(c, self.key) for c in message)

    def decrypt(self, message):
        return ''.join(self.shift_char(c, -self.key) for c in message)

    def key_req(self):
        while True:
            key = input("Enter a key (1-25): ")
            if key.isdigit():
                key = int(key)
                if 1 <= key <= 25:
                    return key
                else:
                    print("Key must be in the range of 1-25.")
            else:
                print("Key must be a number.")

def main():
    message = input("Enter a message: ")
    cipher = CaesarCipher()
    encrypted_message = cipher.encrypt(message)
    print("Encrypted message: " + encrypted_message)
    print("Decrypted message: " + cipher.decrypt(encrypted_message))

if __name__ == "__main__":
    main()