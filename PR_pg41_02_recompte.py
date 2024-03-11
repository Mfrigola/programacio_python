def vote(n):
    x = 0
    y = 0
    z = 0
    for a in range(1,n+1):
        print("Vot número",a,"=",end=" ")
        i = int(input())
        if i == 1:
            x += 1
        elif i == 0:
            y += 1
        else:
            z += 1
    print("Han hagut", x ,"vots a favor,",y,"vots en contra i", z, "vots nuls.")

vote(4)