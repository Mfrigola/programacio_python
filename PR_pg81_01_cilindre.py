#PR_pg81_01_cilindre.py

from math import *

r = float(input("Radi del cilincre: "))
h = float(input("Altura del cilindre: "))

x = 2*pi*r*h+2*pi*pow(r,2)
v = pi*pow(r,2)*h

print("La área del cilinre és: ",x)
print("El volum del cilindre és: ", v)
