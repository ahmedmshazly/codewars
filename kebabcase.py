def kebabize(st):
    st = "".join([i if i.isalpha()==True else "" for i in st])
    l = len(st)
    r = ''
    if l<=3:
        if l==1:
            return st.lower()
        if st.isupper() == True:
            st = st.lower()
            return st[0]+'-'+st[-1] if l == 2 else st[0]+'-'+st[1]+'-'+st[-1]
        elif st.islower() == True:
            return st
        else:
            if l==2:
                return "".join([c+"-" if c.isupper()==True and st[0]==c else c if c.islower()==True else '-'+c.lower() for c in st])     
            else:
                for idx, char in enumerate(st):
                    if idx==0 and char.isupper():
                        r=r+char.lower()+'-'
                    elif idx==0 and char.islower():
                        r=r+char.lower()
                    elif idx==1 and char.isupper() and st[0].isupper()==True:
                        r=r+char.lower()
                    elif idx==1 and char.isupper() and st[0].islower()==True:
                        r=r+'-'+char.lower()
                    else:
                        r=r+char.lower()


    else:
        for idx, char in enumerate(st):
            if char.isalpha()==True:
                if (idx==0):
                    r=r+char.lower()
                elif idx>0 and char.isupper()==True:
                    r=r+'-'+char.lower()
                else:
                    r=r+char.lower()

    return r
                # r=r+char.lower()+ if r.isalpha()==True and st[idx+1].isupper()==True else 
def kebabize(s):
    return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')

print(kebabize("wXf1"))
# print("".join([i if i.isalpha()==True else "" for i in "S3S"]))
