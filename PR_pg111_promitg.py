#PR_pg111_promitg.py

n = int(input("N: "))
p = 0.0
a = 0
for x in range(n):
    p += int(input("Num: "))
p = p/n
print(f"El primitg es: {p}")