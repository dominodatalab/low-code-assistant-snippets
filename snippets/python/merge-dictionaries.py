# Merge two dictionaries into a single dictionary.

# This is the approach which works prior to Python 3.5.
#
def merge_dictionaries_old(first, second):
    first = first.copy()
    first.update(second)
    return first


# This is the approach which works after Python 3.5.
#
def merge_dictionaries_new(first, second):
    return {**first, **second}


merge_dictionaries_old({"age": 25}, {"name": "Joe"})
merge_dictionaries_new({"age": 25}, {"name": "Joe"})
#
# {'age': 25, 'name': 'Joe'}
