add=0
N=int(input())
k=int(input())
monty=[int(input()),int(input()),int(input()),int(input()),int(input())]
for i in range(k):
    add=add+monty[i]
    i+=1
print(add)
