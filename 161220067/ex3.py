m=int(input())
list1=[]
for i in range(m):
    str2=input()
    list2=str2.split()
    list1=list1+list2
n=int(input())
inf=[[0 for i in range(2)]for i in range(n)]
for i in range(n):
    str3=input()
    list3=str3.split()
    inf[i][0]=int(list3[0])
    inf[i][1]=int(list3[1])
#print(inf)
mai=0
zhuan=0
for i in range(m):
    time=int(list1[i*3])
    num=int(list1[i*3+1])
    if list1[i*3+2]=='1':
        jin=0
        for j in range(n):
            if inf[j][0]==time:
                jin=inf[j][1]*num*100
        yong=max(5,jin*0.002)
        guo=num/10
        fee=yong+guo+1
        mai=mai+jin+fee
    else :
        jin=0
        for j in range(n):
            if inf[j][0]==time:
                jin=inf[j][1]*num*100
        yong=max(5,jin*0.002)
        guo=num/10
        fee=yong+guo+1+jin*0.001
        zhuan=zhuan+jin-fee
print(round(zhuan-mai,2))
