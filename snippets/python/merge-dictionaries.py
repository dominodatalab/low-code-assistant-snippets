# Merge two dictionaries into a single dictionary.


def merge_dictionaries(first, second):
    first = first.copy()
    first.update(second)
    return first


merge_dictionaries({"age": 25}, {"name": "Joe"})
#
# {'age': 25, 'name': 'Joe'}
