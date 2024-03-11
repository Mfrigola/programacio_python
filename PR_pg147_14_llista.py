#PR_pg147_14_llista.py
import geometry

def a1():
    l = []
    a = 0
    p = int(input("Presupost: "))
    n = int(input("N llista: "))
    for x in range(1,n+1):
        a = int(input(f"Preu del prducte {x}: "))
        l.append(a)

    for x in range(len(l)):
        if l[x] <= p:
            a = p//l[x]
            print(f"Article {x+1} te un preu de {l[x]}€ i amb el presupost, en pots comprar {a} unitats.")
        else:
            print(f"Article {x+1} te un preu de {l[x]}€ i no entra dintre del presupost de {p}€.")
            























def a2():
    l = []
    a = 0
    p = int(input("Presupost: "))
    n = int(input("N llista: "))
    for x in range(1,n+1):
        a = int(input(f"Preu del prducte {x}: "))
        l.append(a)

    for x in range(len(l)):
        if l[x] <= p:
            a = p//l[x]
            print(f"Article {x+1} te un preu de {l[x]}€ i amb el presupost, en pots comprar {a} unitats.")
        else:
            print(f"Article {x+1} te un preu de {l[x]}€ i no entra dintre del presupost de {p}€.")
