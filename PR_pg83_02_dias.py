#PR_pg83_02_dias.py

from math import *

d = int(input("Dias: "))

m = d//30
mm = d%30//7
dd = d%30%7

print(d,"equival a:",m,"messos",mm,"setmanes i en sobren:",dd,"dies.")