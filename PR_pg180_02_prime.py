import random
def primo():
    x = []
    a = True
    for i in range(1,101):
        for y in range(2,i):
            if i%y==0:
                a = False
        if a and i not in x:
            x += [i]
        a = True
    
    while True:
        a = random.choice(x)
        b = random.choice(x)
        if a+b in x:
            print(f"el numeros primers {a} i {b} sumats donen {a+b}")
            break
        
primo()