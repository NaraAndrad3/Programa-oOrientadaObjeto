lista =[[0],1,[2,[3,4]],5]
l=[]
for i in lista:
    if type(i) != list:
        l.append(i)
    if type(i)==list:
        for item in i: 
            l.append(item)
for i in l:
    if type(i)!=list:
        print(i)
    if type(i)==list:
        for y in i:
            print(y)
