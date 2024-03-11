#PR_pg83_06_bacteries.py

x = int(input("x ="))
m = int(input("m ="))
d = 1
b = 1

while b<m:
    b =2**b*x
    d+=1

print(d)