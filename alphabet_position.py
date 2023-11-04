import string
def alphabet_position(text):
    return "".join([f"{list(string.ascii_lowercase).index(i)+1} " for i in text.lower() if i in string.ascii_lowercase]).strip()

print(alphabet_position("Aaas as"))
# print(string.ascii_lowercase)