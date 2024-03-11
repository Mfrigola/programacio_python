#PR_pg146_04_pi.py
a = 0
b = 1
while b<100000:
    a += 1/b - 1/(b+2)
    b += 4
print(a*4)