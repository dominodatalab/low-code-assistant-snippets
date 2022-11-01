# Merge two lists into a dictionary.

keys = [
    "Asia",
    "Africa",
    "Europe",
    "North America",
    "South America",
    "Australia",
    "Antarctica",
]
values = [31.0, 29.6, 22.1, 21.3, 17.5, 8.5, 13.7]

# Method 1: Zip
#
# 1. Zip lists into a list of tuples.
# 2. Convert list of tuples into a dictionary.
#
dict(zip(keys, values))

# Method 2: List Comprehension
#
{key: value for key, value in zip(keys, values)}
#
# This has the added benefit that you can filter.
#
{key: value for key, value in zip(keys, values) if value > 25}
