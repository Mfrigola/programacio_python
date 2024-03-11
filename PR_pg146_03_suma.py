#PR_pg146_03_suma.py

x = float(input("x = "))

r = 1
a = 1
while x > a:
    a += r**r
    r += 1

print(r)