#PO_pg71_05_dolar.py

p = float(input("Vaor depositat cada any: "))
x = float(input("Valor nominal de interes: "))
n = float(input("número de diposits realitzats"))

a = p*(((1+x)**n-1)/x)

print(a)