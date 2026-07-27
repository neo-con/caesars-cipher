"""A small demonstration of the Caesar cipher.

The cipher shifts each letter a fixed number of places through the alphabet.
Non-letters (spaces, punctuation, digits) are passed through untouched, and
letter case is preserved.
"""


class CaesarCipher:
    """Encrypts and decrypts text with a fixed alphabetic shift."""

    def __init__(self, key):
        # Normalising here means the object is always in a valid state,
        # no matter what the caller passed in: 27 and 1 are the same shift.
        self.key = key % 26

    @staticmethod
    def shift_char(c, key):
        """Shift a single character by `key` places, wrapping around Z -> A."""
        if not c.isalpha():
            return c
        start = ord('A') if c.isupper() else ord('a')
        return chr(start + (ord(c) - start + key) % 26)

    def encrypt(self, message):
        return ''.join(self.shift_char(c, self.key) for c in message)

    def decrypt(self, message):
        # Python's % always returns a non-negative result for a positive
        # modulus, so a negative key wraps correctly with no special casing.
        return ''.join(self.shift_char(c, -self.key) for c in message)


def brute_force(message):
    """Yield (key, plaintext) for every possible key.

    With only 25 keys, a Caesar cipher can be broken by simply trying them
    all -- which is the most useful thing this program can show you.
    """
    for key in range(1, 26):
        yield key, CaesarCipher(key).decrypt(message)


def prompt_for_key():
    """Ask for a key until the user gives a whole number from 1 to 25."""
    while True:
        try:
            key = int(input("Enter a key (1-25): "))
        except ValueError:
            print("Key must be a whole number.")
            continue
        if 1 <= key <= 25:
            return key
        print("Key must be in the range 1-25.")


MENU = """
1) Encrypt a message
2) Decrypt a message
3) Crack a message (try every key)
4) Quit
"""


def main():
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            message = input("Message: ")
            cipher = CaesarCipher(prompt_for_key())
            print("Encrypted:", cipher.encrypt(message))
        elif choice == "2":
            message = input("Message: ")
            cipher = CaesarCipher(prompt_for_key())
            print("Decrypted:", cipher.decrypt(message))
        elif choice == "3":
            message = input("Message: ")
            for key, guess in brute_force(message):
                print(f"{key:2}: {guess}")
        elif choice == "4":
            break
        else:
            print("Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()  # leave the terminal on a clean line