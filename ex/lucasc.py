def hi():
    return 'hi'

def fatorial(n):
    a = n;
    if n == 0:
        return 1
    while n != 1:
        a *= (n -1)
        n -= 1
    return a

def ehPar(n):
    if n%2 == 0:
        return True
    return False
