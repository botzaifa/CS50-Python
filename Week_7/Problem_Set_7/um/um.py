import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    """
    Returns the number of times "um" appears in the input text, case-insensitively, as a word unto itself.
    """
    pattern = r"\bum\b"  # use word boundary (\b) to match "um" as a whole word
    matches = re.findall(pattern, s, re.IGNORECASE)  # use IGNORECASE for case-insensitive match
    return len(matches)


if __name__ == "__main__":
    main()
