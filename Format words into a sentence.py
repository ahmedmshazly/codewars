def format_words(words):
    if words != None:
        words = [item for item in words if item != ""] if len(words)>0 else []
    else:
        return ""
    if len(words)==0:
        return ""
    if len(words)>1:
        return "".join(","+" "+i if idx != len(words)-1 else " and "+i for idx, i in enumerate(words)).strip(" ,")
    else:
        return words[0]
        

print(format_words(None)) 


