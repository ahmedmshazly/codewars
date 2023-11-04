def find_uniq(arr):
    if len(arr)==0:
        return ""
    elif len(arr) == 1:
        return arr[0]
    
    l = [set(i.lower().strip(" ")) for i in arr]
    x=0
    r = ''
    for idx, ele in enumerate(l):
        if l[0] != ele:
            x+=1
            r = arr[idx]

        if x==2:
            return arr[0] 
        elif x==1:
            return r 
        
print(find_uniq([ '    ', 'a', '  ' ]))

        

