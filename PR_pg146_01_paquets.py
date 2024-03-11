x = int(input("n = "))
a = True
pr = 0
me = x
ma = x
np = 0
while a:
    print("Pes paquet",np+1,": ",end="")
    i = str(input())
    if i < me:
        me = i
    if i > ma:
        ma = i
    if i == "Fi":
        a = False
    np += 1
    pr += i

pr = pr/np
print(pr, me, ma)

