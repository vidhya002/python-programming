d=input()
c=0
if d.isdigit():
    d=int(d)
    while(d>0):
        r=d%10
        c=c*10+r
        d=d//10
    print(c)
else:
    print('Invalid Input')
    
