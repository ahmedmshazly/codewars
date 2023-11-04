def autocomplete(input_, dictionary):
    #your code here
    r = []
    s=''
    if input_.strip(" ") == "":
        return dictionary[0:5] if len(dictionary)>5 else dictionary
    if not input_.isalpha():
        for c in input_:
            if c.isalpha():
                s+=c
        if len(s)>0:
            for word in dictionary:
                if word.lower().startswith(s.lower()):
                    r.append(word)
    elif input_.isalpha():
        for word in dictionary:
            if word.lower().startswith(input_.lower()):
                r.append(word)
    else:
        return []
    
    return r[0:5] if len(r)>5 else r

print(autocomplete('*&1i', [ 'abnormal', 'arm-wrestling', 'absolute', 'Airplane', 'airport', 'amazing', 'apple', 'ball' ]))

['abnormal','arm-wrestling','absolute','airplane','airport']
['abnormal', 'arm-wrestling', 'absolute', 'airplane', 'airport', 'amazing', 'apple'] 
['abnormal', 'arm-wrestling', 'absolute', 'airplane', 'airport']

print("a   ".strip(" "))