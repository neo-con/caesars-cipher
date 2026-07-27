# Caesar's Cipher

A Python implementation of the Caesar cipher, one of the oldest known encryption
techniques. Each letter in the message is shifted a fixed number of places
through the alphabet — with a key of 3, `a` becomes `d` and `z` wraps around to
`c`.

Requires Python 3. No dependencies.

```
python Caesars_Cipher-Basic.py
```

## How it works

Each character is checked to see whether it's a letter. If it is, it's anchored
to `'A'` or `'a'` depending on its case, shifted by the key, and wrapped back
into the 26-letter alphabet using modular arithmetic. This keeps uppercase
uppercase and lowercase lowercase. Anything that isn't a letter — spaces,
punctuation, digits — passes through unchanged, which is why word boundaries
stay visible in the output.

Decryption reuses the same routine with a negated key. Python's `%` operator
returns a non-negative result for a positive modulus, so shifting backwards
wraps correctly without any special handling.

## Features

- Encrypts and decrypts messages using a shift key supplied by the user.
- Wraps around the end of the alphabet in both directions.
- Preserves letter case and leaves non-alphabetic characters untouched.
- Re-prompts until the key is a whole number between 1 and 25.

## Example

```
Enter a message: My name is Neo.
Enter a key (1-25): 12
Encrypted message: Yk zmyq ue Zqa.
Decrypted message: My name is Neo.
```

## A note on security

This cipher offers no real protection. There are only 25 possible keys, so any
message can be broken by simply trying all of them and reading whichever result
makes sense. Even without brute force, the cipher maps every occurrence of a
given letter to the same output letter, so the frequency pattern of the original
language survives encryption intact and gives the key away.

Historically, the next development was to vary the shift as it moves through the
message rather than holding it constant — the approach behind the Vigenère
cipher, which uses a keyword to set a different shift for each position.

This project is a learning exercise, not a security tool.