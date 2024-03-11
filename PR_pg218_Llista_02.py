n=int(input('Cuantos elementos: '))
v=[]

for i in range(n):
    x=int(input("N.elements: "))
    v=v+[x]
print('Llista original: ',v)

u = []

for e in v:
    if e not in u:
        u.append(e)
print('Llista depurada: ',u)
