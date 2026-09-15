"""
morse.py

Encodes a string into Morse code.
  - Supports letters (A-Z, case-insensitive), digits (0-9), and spaces.
  - Each Morse character is made of dots '.' and dashes '-'.
  - Complete Morse characters are separated by a single space.
  - A space in the original string is represented by a slash '/'.

Usage:
    python morse.py "SOS"
"""

import sys

MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    ' ': '/',
}


def ft_morse(text):
    try:
        assert isinstance(text, str), \
            "AssertionError: the argument must be a string"
        assert all(c.upper() in MORSE_CODE for c in text), \
            "AssertionError: the string must contain only char characters"

        return ' '.join(MORSE_CODE[c.upper()] for c in text)

    except AssertionError as msg:
        print(msg)
        exit(1)


def main():
    try:
        args = sys.argv[1:]

        assert len(args) == 1, "AssertionError: exactly 1 argument is required"

        print(ft_morse(args[0]))

    except AssertionError as msg:
        print(msg)
        exit(1)


if __name__ == "__main__":
    main()
