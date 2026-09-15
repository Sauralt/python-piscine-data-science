import sys
import string


def analyze(text):
    """
    Analyze the given text and print the counts of various character types.
    """
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())
    punctuation = sum(1 for c in text if c in string.punctuation)

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main(argv):
    """
    Analyze the text provided as a command-line argument.
    """
    try:

        assert len(argv) <= 2, "AssertionError: only one argument is allowed"

        text = argv[1]
        analyze(text)

    except AssertionError as msg:
        print(msg)
        exit(1)


if __name__ == "__main__":
    main(sys.argv)
