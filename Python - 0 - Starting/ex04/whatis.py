import sys


def whatis(number: int) -> str:
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def main(argv):
    try:
        assert len(argv) <= 2, "more than one argument provided"
        assert len(argv) > 1, "no argument provided"
        assert argv[1][0] == "-" and argv[1][1:].isnumeric() \
            or argv[1].isnumeric(), "argument is not an integer"
        for num in argv[1][0]:
            result = whatis(int(num))
            print(f"I'm {result}.")

    except AssertionError as msg:
        print(f'AssertionError: {msg}')
        exit(1)


if __name__ == "__main__":
    main(sys.argv)
