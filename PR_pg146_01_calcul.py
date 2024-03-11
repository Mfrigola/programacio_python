#PR_pg146_01_calcul.py


max = 0.0
min = 999999999.0
r = 0.0
i = 1
n = int(input("Introduei la quantitat de paquets: "))

while i<=n:
    y = float(input(f"Pes del paquet {i:02d}: "))
    r += y
    if y>max:
        max = y
    if y<min:
        min = y
    i += 1
    
r = r/n
print(f"El preu promitg és: {r}, el més baix és: {min} i el més gran: {max}.")