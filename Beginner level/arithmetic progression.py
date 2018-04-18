f,c,n=input().split(" ")
i=1
s=1
for i in range(int(n)+1):
    g=int(f)+(int(i)-1)*int(c)
    s=s+g
print(s)
