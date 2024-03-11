#RO_PO41_5_Suma_de_termes.py

def aab(n):
    x = 0
    i = 0
    while i <= n:
        x += 1
        i += x*x
        print(x,i)
    print(x)
aab(1000)
        