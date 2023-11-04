def alphabet_war(fight):
    r = ''
    scores = {'w':4, 'p':3, 'b':2, 's':1, 'm':-4, 'q':-3, 'd':-2, 'z':-1}
    score = 0
    bomb = lambda idx, c, fight, r: c if fight[idx-1]!='*' and fight[idx+1]!='*' and c.isalpha() else ""
    if len(fight)==1 and fight.isalpha():
        r=fight
    elif len(fight)==1 and not fight.isalpha():
        r = ""
    else:
        for idx, c in enumerate(fight):
            if idx==0:
                r += c if fight[idx+1]!='*' and c.isalpha() else ""
            elif idx==len(fight)-1:
                r += c if fight[idx-1]!='*' and c.isalpha() else ""
            else:
                x = bomb(idx, c, fight, r)
                r = r+x
    
    score = sum(scores[i] if i in list(scores.keys()) else 0 for i in r)
    if score<0:
        return 'Right side wins!'
    elif score>0:
        return 'Left side wins!'
    else:
        return "Let's fight again!"


print(alphabet_war("faawqgg"))

# scores = {'w':4, 'p':3, 'b':2, 's':1, 'm':-4, 'q':-3, 'd':-2, 'z':-1}
# print(list(scores.keys()))