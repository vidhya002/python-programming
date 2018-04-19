n,f,c=input().split(" ")
s=0
for i in range(1,int(n)+1):
    g=int(f)+(int(i)-1)*int(c)
    s=s+g
print(s)
