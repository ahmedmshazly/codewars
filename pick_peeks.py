def pick_peaks(arr):
    
    pleft=0
    pright=2
    current=1

    r = dict({"pos":[], "peaks":[]})

    length = len(arr)

    if length<=2:
        return r
    while pright<length:
        if (arr[current] > arr[pleft]) and (arr[current] > arr[pright]):
            r["pos"].append(current)
            r["peaks"].append(arr[current])
        elif (arr[current] == arr[pright]) and (arr[current] > arr[pleft]):
            while pright<length:
                if arr[pright] == arr[current]:
                    pright+=1
                elif arr[pright] < arr[current]:
                    r["pos"].append(current)
                    r["peaks"].append(arr[current])
                    break
                else:
                    break
            pleft = pright-2
            current = pright-1
            continue 
           

        pleft+=1 
        pright+=1 
        current+=1
        
    return r

print(pick_peaks([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7]))
