str1=input()
n=[0]*2
list1=str1.split()
n[0]=int(list1[0])
n[1]=int(list1[1])
area=[0]*n[0]
str2=input()
list2=str2.split()
for i in range(n[0]):
    area[i]=int(list2[i])
#print(n,area)
flag=100000
for i in range(n[0]):    
        b[0] = i
        for j in range(i+1, n[0]):
            b[1] = j
            for k in range(j+1, n[0]):
                b[2] = k
                for l in range(k+1, n[0]):
                    b[3] = l
                    for m in range(l+1,n[0]):
                        b[4]=m
