count=0
g=int(input())
for i in range(2,g):
    if(g%i==0):
        count+=1
if(count==0):
    print("yes")
else:
    print("no")
