def take(count, iterable):
    """Take items from the front of an iterable.

    Args:
        count: The maximum number of items to retrieve.
        iterable: The source of the items.

    Yields:
        At most 'count' items from 'iterable'.
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return

        counter += 1

        yield item


def run_take():
    items = [2, 4, 6, 8, 10, 20, 30, 40, 50]

    # normal execution to print all the i's of the items list

    for i in items:
        print(i)

    # to print only the 1st 3 elements of the list(iterable object)

    for i in take(3, items):
        print(i)


if __name__ == "__main__":
    run_take()
