def add(a,b):
    c = a - b
    return c

def multiply(n):
    if n < 0:
        raise ValueError('No factorial for negative number')
    elif n == 0:
        return 1
    else:
        kq = 1
        for i in range(1,n+1):
            kq *=i
        return kq