b=str(input())
b=b.lower()
g=length(b)
h=[]
for i in range(1,g):
    h.append(b[-i])
h.append(b[0])    
for i in h:
    if i=='a':
        h.replace(i,"")
    elif i=='e':
        h.replace(i,"")
    elif i=='i':
        h.replace(i,"")
    elif i=='o':
        h.replace(i,"")
    elif i=='u':
        h.replace(i,"")
k="".join(h)
print(k)   
