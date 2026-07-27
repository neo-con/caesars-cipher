"""A small demonstration of the Caesar cipher.

The cipher shifts each letter a fixed number of places through the alphabet.
Non-letters (spaces, punctuation, digits) are passed through untouched, and
letter case is preserved.
"""

from collections.abc import Iterator
from dataclasses import dataclass
from enum import StrEnum


@dataclass(slots=True)
class CaesarCipher:
    """Encrypts and decrypts text with a fixed alphabetic shift."""

    key: int

    def __post_init__(self) -> None:
        # Normalising here means the object is always in a valid state,
        # no matter what the caller passed in: 27 and 1 are the same shift.
        self.key %= 26

    @staticmethod
    def shift_char(c: str, key: int) -> str:
        """Shift a single character by `key` places, wrapping around Z -> A."""
        if not c.isalpha():
            return c
        start = ord('A') if c.isupper() else ord('a')
        return chr(start + (ord(c) - start + key) % 26)

    def encrypt(self, message: str) -> str:
        return ''.join(self.shift_char(c, self.key) for c in message)

    def decrypt(self, message: str) -> str:
        # Python's % always returns a non-negative result for a positive
        # modulus, so a negative key wraps correctly with no special casing.
        return ''.join(self.shift_char(c, -self.key) for c in message)


def brute_force(message: str) -> Iterator[tuple[int, str]]:
    """Yield (key, plaintext) for every possible key.

    With only 25 keys, a Caesar cipher can be broken by simply trying them
    all -- which is the most useful thing this program can show you.
    """
    for key in range(1, 26):
        yield key, CaesarCipher(key).decrypt(message)


def prompt_for_key() -> int:
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


class Choice(StrEnum):
    ENCRYPT = "1"
    DECRYPT = "2"
    CRACK = "3"
    QUIT = "4"


MENU = """
1) Encrypt a message
2) Decrypt a message
3) Crack a message (try every key)
4) Quit
"""


def main() -> None:
    while True:
        print(MENU)
        # StrEnum members compare equal to their string values, so the raw
        # input can be matched against the enum directly.
        match input("Choose an option: ").strip():
            case Choice.ENCRYPT:
                message = input("Message: ")
                cipher = CaesarCipher(prompt_for_key())
                print("Encrypted:", cipher.encrypt(message))
            case Choice.DECRYPT:
                message = input("Message: ")
                cipher = CaesarCipher(prompt_for_key())
                print("Decrypted:", cipher.decrypt(message))
            case Choice.CRACK:
                message = input("Message: ")
                for key, guess in brute_force(message):
                    print(f"{key:2}: {guess}")
            case Choice.QUIT:
                break
            case _:
                print("Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()  # leave the terminal on a clean line
