j=input()
a=0
if j.isdigit():
    j=int(j)
    while(j>0):
        r=j%10
        a=a+r*r
        j=j//10
    print(a)
else:
    print('Invalid Input')
