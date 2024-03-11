#PR_pg146_04_suma.py

from random import*
x=0
y=0
i=0
while -5<x<5 and -5<y<5:
    d=randint(1,4)
    i=i+1
    if d==1:
        x=x+1
    elif d==2:
        x=x-1
    elif d==3:
        y=y+1
    else:
        y=y-1
    print(x,y)
print('Cantidad de intentos: ',i)
i = input('Cantidad de intentos: ')