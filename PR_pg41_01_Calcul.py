#RO_PO41_01_Calcul.py
def aab():
    n = int(input("n. paquets = "))
    pm = 0
    pp = 0
    np = 0
    for x in range(1,n+1):
        print("Pes paquet n.",x,"en Kg =", end =" ")
        pp = int(input())
        if pp > pm:
            pm = pp
            np = x
        
    print("El n. del paquet més pesat és el",np,"amb un pes de",pm,"Kg")

def bba():
    n = int(input("n. paquets = "))
    pm = 0
    pp = 0
    np = 0
    i = 1
    while i <= n:
        print("Pes paquet n.",i,"en Kg =", end =" ")
        pp = int(input())
        if pp > pm:
            pm = pp
            np = i
        i +=1
        
    print("El n. del paquet més pesat és el",np,"amb un pes de",pm,"Kg")

bba()
