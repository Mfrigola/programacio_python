#PR_pg081_09_triangle.py

from math import *

px = int(input("Introdueix la px: "))
py = int(input("Introdueix la py: "))
qx = int(input("Introdueix la qx: "))
qy = int(input("Introdueix la qy: "))
x = sqrt(pow(px,2)+pow(py,2))
y = sqrt(pow(qx,2)+pow(qy,2))
t = (x+y+z)/2
s = sqrt(t*(t-x)+(t-y)*(t-z))
print("L'area del triangle és: ",s)