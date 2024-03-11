#PR_pg148_24_algo.py

import random

n = int(input("N vegades = "))
r = 0
a = 0

for x in range(n):
    a = random.randint(1,6)
    if a == 6:
        r += 5
        print(f"La tirada {x+1} a tingut un resultat de 6, per tant, has guanyat 5$ i tens {r}$")
    if a == 1:
        r += 1
        print(f"La tirada {x+1} a tingut un resultat de 1, per tant, has guanyat 1$ i tens {r}$")
    else:
        r -= 25
        print(f"La tirada {x+1} a tingut un resultat de {a}, per tant, has perdut 2$ i tens {r}$")