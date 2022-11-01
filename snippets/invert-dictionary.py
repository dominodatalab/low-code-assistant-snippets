# Invert a dictionary.

capitals = {
    "England": "London",
    "Scotland": "Edinburgh",
    "Wales": "Cardiff",
}

# Inverting a dictionary interchanges the keys and values.

dict(map(reversed, capitals.items()))
