#!/home/aditya/miniconda3/bin/python

# adding doc strings for help()
"""Retrieve and print words from a URL.

Usage:

python3 words.py <URL>

"""

import sys

from urllib.request import urlopen


def fetching(url):
    # adding doc strings to a function so that we can search for help
    """Fetch a list of words from a URL.

    Args:
    url: The URL of a UTF-8 text document.

    Returns:
    A list of strings containing the words from
    the document.
    """

    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    return story_words


def printing(story_words):
    """Print items one per line.

    Args:
    items: An iterable series of printable items.
    """

    for word in story_words:
        print(word)


def main(url):
    """Print each word from a text document at a URL.

    Args:
    url: The URL of a UTF-8 text document.
    """
    wordslist = fetching(url)
    printing(wordslist)


if __name__ == "__main__":  # only on terminal or ide
    print(
        """This if statement will get satisfied only from the command line or the ide but not while importing this module from the repl""")
    main(sys.argv[1])  # 0th argument is the module file name


elif __name__ == "words_commandline_repl":  # only on the repl : name of the module
    print(
        "this statement will get executed only when the module is imported from the repl and not when this module is run from the terminal or ide")
