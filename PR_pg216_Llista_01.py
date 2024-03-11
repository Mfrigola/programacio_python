n = int(input("N.elements: "))
v = []

for i in range(n):
    x = int(input("Element {i+1}: "))
    v.append(x)

s = 0
for e in v:
    if e%2==0:
        s += e

print("La sum es: s")