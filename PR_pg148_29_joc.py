#PR_pg148_29_joc.py

a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

r = a + b + c
q=0
print(r)

while r>=10:
    for x in str(r):
        q += int(x)
    r = q
    q = 0
    print(r)
