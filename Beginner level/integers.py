add=0
v=int(input())
m=int(input())
monty=[int(input()),int(input()),int(input()),int(input()),int(input())]
for i in range(m):
    add=add+monty[i]
    i+=1
print(add)
