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


def distinct(iterable):
    """Return unique items by eliminating duplicates.

    Args:
        iterable: The source of the items.

    Yields:
        Unique elements in order from 'iterable'.
    """

    seen = set()

    indexer = 0  # to check that the element from which index is taken up in seen

    for item in iterable:

        if item in seen:
            indexer += 1
            continue

        print("yielding item : ", item)
        print("indexer = ", indexer)
        yield item
        seen.add(item)
        indexer += 1

    print("Distinct elements : ", seen)


def run_pipeline1():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


def run_pipeline2():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, list(distinct(items))):
        print(item)


if __name__ == "__main__":
    run_pipeline1()
    for i in range(10):
        print()

    run_pipeline2()
