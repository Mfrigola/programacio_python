#RO_PO41_4_Valor_pi.py

def abb():
    r = 0
    a = 1
    b = 0
    for x in range(1,1000000000,2):
        if a == 1:
            r += 1/x
            a = 0
        else:
            r -= 1/x
            a = 1
            
    print(r*4)



abb()