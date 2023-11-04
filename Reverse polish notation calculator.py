def calc(expr):
    stack = []
    s = int()
    if len(expr) == 0:
        return 0
    elif len(expr) == 1:
        return int(expr)
    elif len(str(expr).split(".")) == 2:
        return float(expr)
    
    # Cases of expr
    x = 0
    y = 0
    n = ""
    for idx, i in enumerate(expr):
        try:
            if expr[idx+1].isnumeric() and i != " ":
                n = n + i
                continue
            elif not expr[idx+1].isnumeric() and expr[idx-1].isnumeric():
                n = n + i
                i = n
        except:
            pass
        if str(i).isnumeric():
            try:
                if expr[idx+1] == ".":
                    stack.append(float(expr[idx:idx+3]))
                    x+=1
                elif expr[idx-1] == ".":
                    pass
            except IndexError:
                stack.append(int(i))
                x+=1
            else:
                stack.append(int(i))
                x+=1
            y=0
            n=""
        elif i in ['+', '-', '*', '/']:
            y+=1
            if x >= 2:
                match i:
                    case '+':
                        s+=stack[-2]+stack[-1]
                    case '-':
                        s+=stack[-2]-stack[-1]
                    case '*':
                        s+=stack[-2]*stack[-1]
                    case '/':
                        s+=stack[-2]/stack[-1]
                if len(stack) > 0:
                    stack.pop()
                    stack.pop()

            elif x == 1 or y >1:
                match i:
                    case '+':
                        s+=stack[-1]
                    case '-':
                        s-=stack[-1]
                    case '*':
                        s*=stack[-1]
                    case '/':
                        s/=stack[-1]
                if len(stack) > 0:
                    stack.pop()
            x=0
    if '.0' in str(s):
        return int(s)
    else:
        return s
                

print(calc('500 1 2 + 4 * + 3 -'))
print("ssssdd"[:-2])