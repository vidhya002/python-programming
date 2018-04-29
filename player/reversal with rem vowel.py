b=str(input()))
b=b.lower()
c=('a','e','i','o','u')
for i in b:
    if i in c:
        b=b.replace(i,"")
        d=b[::-1]
        print(d)
if i not in c:
    print(b[::-1])
