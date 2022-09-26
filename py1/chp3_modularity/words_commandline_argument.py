import sys

from urllib.request import urlopen

def fetching(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                 story_words.append(word)

    return story_words


def printing(story_words):
    for word in story_words:
        print(word)

def main():
    url=sys.argv[1]
    wordslist=fetching(url)
    printing(wordslist)



if __name__ == "__main__": # only on terminal or ide
    print("""This if statement will get satisfied only from the command line or the ide but not while importing this module from the repl""")
    main()


elif __name__=="words_commandline_argument": # only on the repl
    print("this statement will get executed only when the module is imported from the repl and not when this module is run from the terminal or ide")



