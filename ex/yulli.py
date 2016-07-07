def hi():
    return 'hi'

def fatorial(n):
    i=n-1
    if n == 0:
        return 1
    while i > 1:
        n *= i
        i -= 1
    return n

def ehPar(n):
    if n%2 == 0:
        return True
    else:
        return False

def divideString(a):
    return a.split(' ')
def inverso(n):
    n = str(n)
    p = ''
    for i in range(len(n)-1,-1,-1):
        p+= n[i]
    return int(p)
