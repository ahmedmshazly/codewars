class example:
    def __init__(self, x, y):
        pass

# def abbreviate(s):
#     temp_words = str(s).split(" ")
#     words = []
#     track = dict()
#     # Make the words list

#     if len(temp_words) == 0:
#         return ""
#     elif len(temp_words) == 1 and len(temp_words[0].split("-")) ==1:
#         return alg(temp_words)

#     for idx, i in enumerate(temp_words): 
#         if "-" in i:
#             track[idx+1] = "-"
#             x = i.split("-")
#             for idx, j in enumerate(x):
#                 words.append(j)
#                 if idx == len(x) -1:
#                     pass
#                 else:
#                     words.append("-")
#         else:
#             words.append(i.strip() if i != "" or i != " " else 0)   
    
#     return alg(words)
    
# def alg(words):
#     r = []
#     # split teh non aplpha 
#     for idx, word in enumerate(words):
#         if word.isalpha():
#             if len(word) <=3:
#                 r.append(word)
#             else:
#                 r.append("".join([word[0], str(len(word)-2), word[-1]]))
#             try:
#                 if words[idx+1] != "-":
#                     r.append(" ")
#             except:
#                 pass
#         elif word[0].isalpha() and not word[-1].isalpha:
#             if len(word) <=3:
#                 r.append(word)
#             else:
#                 r.append("".join([word[0], str(len(word)-3), word[-2]]))
#             try:
#                 if words[idx+1] != "-":
#                     r.append(" ")
#             except:
#                 pass
#         else:
#             r.append(word)
#     return "".join(r)

            
import re

regex = re.compile('[a-z]{4,}', re.IGNORECASE)

def replace(match):
    word = match.group(0)
    print(word)
    return word[0] + str(len(word) - 2) + word[-1]

def abbreviate(s):
    return regex.sub(replace, s)

def abbreviate(s):
    mutate = lambda w: w[0] + str(len(w) - 2) + w[-1] if len(w) > 3 else w
    result, word = '', ''
    for char in s:
        if char.isalpha():
            word += char
        else:
            result += mutate(word) + char
            word = ''
    result += mutate(word)
    return result

# print(abbreviate("elephant-rides are really fun!"))
print(abbreviate("elephant-ride"))
print("aa!".isalpha())


