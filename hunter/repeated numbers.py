n=int(input())
list1=[]
list2=[]
count=0
for i in range(0,n):
    r=int(input())
    if(type(r)==int):
        list1.append(r)
for j in range(0,n):
    c=list1.count(list1[j])
    if(c>1):
        if(list1[j] not in list2):
            list2.append(list1[j])
            count=count+1
if(count>=1):
    print(sorted(list2))
