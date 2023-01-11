# Extract only unique elements from a list.


def to_unique(lst):
    """Remove duplicates from a list."""
    return list(set(x))


def is_unique(lst):
    """Check whether items in a list are unique."""
    return len(lst) == len(set(lst))


unique = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
duplicates = [1, 1, 1, 3, 3, 5, 5, 5, 7, 8, 9]

is_unique(unique)  # True
is_unique(duplicates)  # False

# Remove duplicates.
#
deduplicated = to_unique(duplicates)

is_unique(deduplicated)  # True
