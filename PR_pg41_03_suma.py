#RO_PO41_3_suma.py

def sum(n):
    suma = 1
    a = 1
    b = 0
    for x in range(1,n+1):
        print(suma)
        b += a
        a = suma
        suma = b

sum(10)

