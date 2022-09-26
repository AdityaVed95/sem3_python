import sys


def convert(s):
    """Convert a string to an integer."""
    try:
        return int(s)

    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        return -1


def main():
    print(convert(34))
    print(convert("abc"))
    print(convert([3, 4, 5]))


if __name__ == "__main__":
    main()
