# 1

def conteo():
    r = 0
    m = []
    ra = 0
    for x in range(1,101):
        for y in range(1,101):
            if x%y == 0:
                r += 1
        if r > ra:
            m = [x]
            ra = r
        elif r == ra:
            m += [x]
        r = 0
            
    return f"els números amb més divisors, són: {x} amb {ra} divisors"

print(conteo())
