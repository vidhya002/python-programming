candy=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
b=input()
if b.isdigit():
    print('Invalid Input')
else:
    b=str(b)
    if(b==candy[0] or b==candy[6]):
        print('yes')
    else:
        print('no')
