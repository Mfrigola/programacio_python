#PR_pg146_02_calcul.py

# Clasifique los pesos de los n objetos de una bodega en tres grupos: menor a 10 Kg.,
# entre 10 y 20 Kg., mas de 20 Kg. Los datos ingresan uno a la vez en un ciclo.


a = True
while a:
    n = float(input("Pes del producte amb Kg: "))
    
    if n=="Fi"or n=="" or n==" ":
        a = False
    else:
        if 0<n<10:
            print("Grup 1")
        elif 10<n<20:
            print("Grup 2")
        else:
            print("Grup 3")