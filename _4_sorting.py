l = [(2,5),(1,4),(4,4),(2,3),(2,1),(3,0),(5,8)]

for i in range(len(l)):
    for j in range(len(l)):
        if l[i][1] <  l[j][1]:
            l[i],l[j] = l[j],l[i]

print(l)                        