def hex_string_to_RGB(hex_string): 
    # your code here\
    r =dict()
    hex_string = hex_string[1:]
    calc = lambda hex, idx: int(hex[idx-1], base=16)*16+int(hex[idx], base=16)
    for idx, pair in enumerate(hex_string):
        if (idx+1)%2 == 0:
            if idx+1 == 2:
                r['r']=calc(hex_string, idx)
            if idx+1 == 4:
                r['g']=calc(hex_string, idx)
            if idx+1 == 6:
                r['b']=calc(hex_string, idx) 
    return r