from math import *
#PR_convertir

def polar(x,y):
    r = (x**2+y**2)**0.5
    t = atan2(y,x)
    return r,t

def cartesiana(r,t):
    x = r*cos(t)
    y = r*sin(t)
    return x,y


def main():
    while True:
        print("1 -- Polar")
        print("2 -- Cartesiana")
        print("3 -- Exit")

        x = input("Ingresa una opcció: ")

        if x == "1":
            print("Has triat polars: ")
            x = int(float(input("Valor x: ")))
            y = int(float(input("Valor y: ")))
            return polar(x,y)
        elif x == "2":
            print("Has triat cartesians:")
            r = int(float(input("Valor r: ")))
            t = int(float(input("Valor t: ")))
            return cartesiana(r,t)
        elif x == "3":
            print("Has desidit tancar el programa.")
            break
        else:
            print("Resposta no válida.")

main()