def damaged_or_sunk (board, attacks):
    ans = dict({ 'sunk': 0, 'damaged': 0 , 'not_touched': 0, 'points': 0})
    def unique(list1):
 
        # initialize a null list
        unique_list = []
    
        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)
        return unique_list
    
    l=[i for j in board for i in j]
    uniques = unique(l)
    uniquesDict = dict()
    for n in uniques:
        uniquesDict[n] = int(l.count(n))
    
    newDict = dict()
    for attack in attacks:
        n = board[abs(attack[1]-len(board))][abs(attack[0]-1)]
        if n!=0:
            if n not in list(newDict.keys()):
                newDict[n] = uniquesDict[n]-1
            else:
                newDict[n] = newDict[n]-1
    
    for rest in list(uniquesDict.keys()):
        if rest not in list(newDict.keys()) and rest !=0:
            newDict[rest] = uniquesDict[rest]
    # return newDict, uniquesDict

    for key in uniquesDict:
        if key in list(newDict.keys()):
            if newDict[key]!=0:
                if newDict[key] < uniquesDict[key]:
                    ans['damaged'] +=1
                    ans['points'] +=0.5
                else:
                    ans['not_touched'] +=1
                    ans['points'] -=1

            else:
                ans['sunk'] +=1
                ans['points'] +=1
     
    return ans
            

                

print(damaged_or_sunk([ [3, 0, 1],
                        [3, 0, 1],
                        [0, 2, 1], 
                        [0, 2, 0] ], 
                        
                        [[2, 1], [2, 2], [ 3, 2], [3, 3]]))