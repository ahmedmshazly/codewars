def sort_the_inner_content(words):
    s = ''
    for i in words.split(" "):
        i2 = list(i[1:-1])
        i2.sort()
        i2.reverse()
        s+="".join(i[0]+"".join(i2)+i[-1]+" " if len(i)>=4 else i+" ")
    return s.strip()



i = "sort"
# print(list(i[1:-1]).sort())
# print(i[0]+i[1:-1][::-1]+i[-1])
# print(i[0]+i[-1:0]+i[-1]+" ")
print(sort_the_inner_content("sort the inner content in descending order"))