#PR_pg83_01_dias.py

from math import *

d = int(input("Dias: "))

a = d//365
m = d%365//30
dd = d%365%30
print(d,"diss equivalen a:",a,"anys,",m,"messos, i",dd,"dies.")