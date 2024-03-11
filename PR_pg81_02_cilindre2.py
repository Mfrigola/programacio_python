#PR_pg81_02_cilindre2.py
from math import *

v = float(input("El volum del recipient és: "))
h = float(input("La altura del recipient és: "))

d = 2*sqrt((v/(pi*h)))

print("El diametre és: ", d)