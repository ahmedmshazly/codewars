# 1- Character --> a. within the range = add OR out of range = 


from string import ascii_lowercase
lower = ascii_lowercase
l_lower = len(lower)
def play_pass(s, n):
    r = []
    if s == "" or s == " ":
        return s
    for i, letter in enumerate(s):
        if letter.isalpha():
            shift = lower.index(letter.lower()) + n
            if shift < l_lower :
                r.append(lower[shift].upper()) if i %2 == 0 or i == 0 else r.append(lower[shift].lower())
            else:
                r.append(lower[shift - l_lower].upper()) if i %2 == 0 or i == 0 else r.append(lower[shift - l_lower].lower())
                
        elif letter.isdigit():
            r.append(str(9 - int(letter)))
        else:
            r.append(letter)
    return "".join(r)[::-1]

# print(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2))
# print("4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO" == "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO")


print(   play_pass("I LOVE YOU!!!", 1) == "!!!vPz fWpM J")    
print(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2) == "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO")
print(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2))
print("4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO")
