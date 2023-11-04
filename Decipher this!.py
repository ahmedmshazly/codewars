import re

def decipher_this(s):
    s2 = ""
    l = [[chr(int(i)) if i.isnumeric() else i[-1]+i[1:-1]+i[0] if len(i) >=2 else i for i in re.split('(\d+)',x)] for x in s.split(" ")]
    for word in l:
        s2+="".join(word)+" "
    
    return s2.strip()
    # return "".join([chr(int(i)) if i.isnumeric() else i[-1]+i[1:-1]+i[0] if len(i) >=2 else i for i in re.split('(\d+)',x)] for x in s.split(" ")) 

print(decipher_this('65 119esi 111dl 111lw 108dvei 105n 97n 111ka'))


