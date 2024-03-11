#PR_pg103_Dau.py

import random

d = 0
c = 0

while True:
    d = random.randint(1,6)
    c += 1
    if d == 3:
        break
    
print(c)