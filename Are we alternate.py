def is_alt(s):
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(s)-1):
        if (s[i] in vowels and s[i+1] in vowels) or (s[i] not in vowels and s[i+1] not in vowels):
            return False
    return True
                

print(is_alt("banana"))