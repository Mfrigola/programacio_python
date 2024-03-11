# 21


def f1(n):
    r = 0
    l = 0
    for x in range(1,n+1):
        r += x
        l += r
        print(x, r)
    print(x,r,l)
    return l

def f2(n):
    r = 0
    i = 1
    while i <= n:
        r += i
        i += 1
        print(r)


    
def f3(n):
    a = f1(n)
    r = 0
    y = 0
    for x in range(1,n+1):
        r += x
        y += a
        print(x,r,y)




f3(10)


    