# Remove "falsy" items (False, None, 0 and "") from a list.


def remove_falsy(lst):
    return list(filter(None, lst))


remove_falsy([1, False, 2, 0, 3, "", 4, None, 5])
#
# [1, 2, 3, 4, 5]
