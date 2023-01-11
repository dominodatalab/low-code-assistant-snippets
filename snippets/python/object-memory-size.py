# Find size of an object in memory.

import sys


def object_size(obj):
    """Return size of object in bytes. This will only work reliably for builtin types."""
    return sys.getsizeof(obj)


object_size(2)
object_size([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
