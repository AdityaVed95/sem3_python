count = 0  # this count is a global variable


def show_count():
    print(count)


def set_count(c):
    global count
    count = c
