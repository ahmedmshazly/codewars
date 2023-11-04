# 1- the existence of the element
# 2- compare the number of the element
def scramble(s1, s2):
    return False if False in [False if s1.count(letter) < s2.count(letter) else True for letter in s2  ] else True
    # return (letter for letter in s2 in s1)

# print(scramble('rkqodlw', 'world'))
print(scramble('npouveiexthf', 'vnpn'))
# print(scramble('rkqodlw', 'world'))

def test():
    for i in 'xhyfhmmkeyxmt':
        if i in 'vzeqtizeqvzxeadtbv':
            pass
        else:
            return False
        return True

def test(s):
    d = dict()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d    
# print(test("vzzedtaevtbaz"))
