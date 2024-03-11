#RO_PO38_ProvaFor.py
n = int(input("n= "))
s = 0

for i in range(1,n+1):
    k = 2*i -1
    s = s + k
    print(k,s)

if s == n**2:
    print(True)
else:
    print(False)
