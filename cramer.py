#matriu

def matriu():
    b = []
    c = []
    while True:
        a = int(input("""Taules:
                       
    1. -   2 x 2
    2. -   3 x 3

    Introduir una opció: """))
        
        if a == 1 or a == 2:
            break
        else:
            print("El valor introduit no es valid, torna-ho a probar")
    a += 1
    print("\n")

    for x in range(a):
        for y in range(a):
            d = int(input(f"N. array m{x+1,y+1}: "))
            c.append(d)
        c += [[int(input("Resultat d'aquesta fila: "))]]
        b.append(c)
        c = []

    print("\n")

    for x in b:
        print(x)

    print("\n")

    if a == 2:

        z = b[0][0] * b[1][1] - b[1][0] * b[0][1]
        x = (b[0][2][0] * b[1][1] - b[1][2][0] * b[0][1]) / z
        y = (b[0][0] * b[1][2][0] - b[1][0] * b[0][2][0]) / z

        print(f"""z = {z}
x = {x}
y = {y}""")
        
    elif a == 3:

        z = (b[0][0] * b[1][1] * b[2][2]  +  b[1][0] * b[2][1] * b[0][2]  +  b[0][1] * b[1][2] * b[2][0]) - (b[2][0] * b[0][2] * b[1][1] + b[1][0] * b[0][1] * b[2][2] + b[2][1] * b[1][2] * b[0][0])
        x = ((b[0][3][0] * b[1][1] * b[2][2]  +  b[1][3][0] * b[2][1] * b[0][2]  +  b[0][1] * b[1][2] * b[2][3][0]) - (b[2][3][0] * b[0][2] * b[1][1] + b[1][3][0] * b[0][1] * b[2][2] + b[2][1] * b[1][2] * b[0][3][0])) / z
        y = ((b[0][0] * b[1][3][0] * b[2][2]  +  b[1][0] * b[2][0][0] * b[0][2]  +  b[0][3][0] * b[1][2] * b[2][0]) - (b[2][0] * b[1][3][0] * b[0][2] + b[1][0] * b[0][3][0] * b[2][2] + b[2][3][0] * b[1][2] * b[0][0])) / z
        zz = ((b[0][0] * b[1][1] * b[2][3][0]  +  b[1][0] * b[2][1] * b[0][3][0]  +  b[0][1] * b[1][3][0] * b[2][0]) - (b[2][0] * b[0][3][0] * b[1][1] + b[1][0] * b[0][1] * b[2][3][0] + b[2][1] * b[1][3][0] * b[0][0])) / z

        print(f"""z = {z}
x = {x}
y = {y}
zz = {zz}""")





matriu()