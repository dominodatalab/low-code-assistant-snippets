# Sort a list of dictionaries.

continents = [
    {"continent": "Asia", "area": 31.0, "population": 3261},
    {"continent": "Africa", "area": 29.6, "population": 1341},
    {"continent": "Europe", "area": 22.1, "population": 748},
    {"continent": "North America", "area": 21.3, "population": 592},
    {"continent": "South America", "area": 17.5, "population": 431},
    {"continent": "Australia", "area": 8.5, "population": 43},
    {"continent": "Antarctica", "area": 13.7, "population": 0},
]

# There are two approaches to sorting:
#
# - sort in place using .sort() method or
# - return sorted list using sorted() function.

# Method 1: Sort in place
#
# Sort in place by (increasing) area.
#
continents.sort(key=lambda item: item.get("area"))
#
# Sort in place by (decreasing) population.
#
continents.sort(key=lambda item: item.get("population"), reverse=True)

# Method 2: Return sorted list
#
# Sort by (increasing) area.
#
sorted(continents, key=lambda item: item.get("area"))
#
# Sort by (decreasing) population.
#
sorted(continents, key=lambda item: item.get("population"), reverse=True)
