n=int(input())
temp=0
arr=[int(input())for x in range(n)]
size=len(arr)
for i in range (0, size):
    for j in range (i + 1, size):
        if arr[i] == arr[j]:
            print(arr[i], end = ' ')
            length=len(arr[i])
            for y in range (0,length):
                for z in range (x + 1,length):
                    if arr[y] > arr[z]:
                        z=y
                        temp=z
                        y=temp
            print(arr[y], end = ' ')
