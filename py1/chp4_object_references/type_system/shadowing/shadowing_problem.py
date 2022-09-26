count = 0  # this count is a global variable


def show_count():
    print(count)


def set_count(c):
    count = c

# the error here says that :
# We have created a new variable which shadows, and thereby prevents access to, the global of the same name.

# import from repl and run
