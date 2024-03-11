#RO_PO41_6_Chess.com.py

def Chess_com():
    r=0
    for x in range(1,65):
        print(x)
        r += 2**x
    r = r/20000000
    print("Haurien necessitat:",r,"Tonalades d'arros.")


Chess_com()