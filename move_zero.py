def move_zeros(lst):    
    return [i for i in lst if i!=0]+[j for j in lst if j==0]

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))