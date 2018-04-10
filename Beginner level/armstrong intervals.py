m,n=input().split(" ")
for i in range(int(m)+1,int(n)):
    temp=i
    c=0
    while(i>0):
        r=i%10
        c=c+r*r*r
        i=i//10
    if(c==temp):
        print(temp,end=' ')
