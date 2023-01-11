# Break list into chunks of specified length.


def chunk(lst, size=1):
    return [lst[i : i + size] for i in range(0, len(lst), size)]


chunk([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
#
# [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

chunk([1, 2, 3])
#
# [[1], [2], [3]]
