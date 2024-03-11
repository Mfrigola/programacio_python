#PR_pg96_12_Local.py

x = int(input("n paquets: "))
y = float(input("preu per unitat: "))

if x<5:
    print(x*y)
elif 5<=x<9:
    print(x*y*0.95)
else:
    print(x*y*0.92)
    