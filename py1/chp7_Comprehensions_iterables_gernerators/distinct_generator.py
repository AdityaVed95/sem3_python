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


def run_distinct():
    items = [5, 7, 7, 6, 5, 5]

    for i in items:
        print(i)

    for i in distinct(items):  # call to the generator function which returns/yields elements one at a time
        print(i)


if __name__ == "__main__":
    run_distinct()

# code from the book :
# def distinct(iterable):
#     """Return unique items by eliminating duplicates.
#
#     Args:
#         iterable: The source of the items.
#
#     Yields:
#         Unique elements in order from 'iterable'.
#     """
#
#     seen = set()
#
#     for item in iterable:
#         if item in seen:
#             continue
#
#         yield item
#         seen.add(item)
#
#     print("Distinct elements : ", seen)
#
#
# def run_distinct():
#     items = [5, 7, 7, 6, 5, 5]
#
#     for i in items:
#         print(i)
#
#     for i in distinct(items):
#         print(i)
#
#
# if __name__ == "__main__":
#     run_distinct()
