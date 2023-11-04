def to_underscore(string):
    string = str(string)
    return "".join([c if (c.islower() or c.isnumeric()) else f"_{c.lower()}" for c in string]).lstrip("_") if string.isalnum() or string.isalpha() else str(string)

# print("7".isupper())
print(to_underscore('App7Test'))