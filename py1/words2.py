#! /home/aditya/miniconda3/envs/py3.10/bin/python


from urllib.request import urlopen


def fetching():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

        for word in story_words:
            print(word)


if __name__ == "__main__":  # only on terminal or ide
    print(
        """This if statement will get satisfied only from the command line or the ide but not while importing this module from the repl""")
    fetching()
if __name__ == "words2":  # only on the repl
    print(
        "this statement will get executed only when the module is imported from the repl and not when this module is run from the terminal or ide")
