n=int(input())
time=[0]*n
str1=input()
list1=str1.split()
for i in range(n):
    time[i]=int(list1[i])
a1=0
b1=0
c1=0
flag1=0
flag2=0
flag3=0
sum2=0
for i in range(n):
    if i%3==0:
        sum2+=a1
        a1+=time[i]
        flag1+=a1
    if i%3==1:
        sum2+=b1        
        b1+=time[i]
        flag2+=b1
    if i%3==2:
        sum2+=c1
        c1+=time[i]
        flag3+=c1
    #print(sum2)
    #print(a1,b1,c1)
m=max(a1,b1,c1)
print(sum2,m)
a=0
b=0
c=0
f1=0
f2=0
f3=0
sum1=0
for i in range(n):    
    if a<=b and a<=c:
        sum1+=a
        a+=time[i]
        f1+=a
    elif b<a and b<=c:
        sum1+=b
        b+=time[i]
        f2+=b
    elif c<b and c<a:
        sum1+=c
        c+=time[i]
        f3+=c
    #print(a,b,c)
print(sum1,max(a,b,c))
            
