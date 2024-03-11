#PR_pg104_sum.py

n = int(input("valur: "))
s = 0
i = 0
while i <= n:
    s = s + i**2
    i = i + 1
print(f"La suma es: {s}")