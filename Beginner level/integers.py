add=0
i=k
k=int(input())
monty=[1,2,3,4,5]
x=monty[:i]
for i in range(k):
    add=add+x[i]
    i-=1
print(add)
