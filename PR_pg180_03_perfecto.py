


def perfecto(n):
    r = 0
    m = 0
    ra = 0
    for y in range(1,n):
        if n%y == 0:
            r += y
    return "El numero es perfecte" if r == n else "El numero no es perfecte"
                
print(perfecto(28))