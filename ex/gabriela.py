def hi():
    return 'hi'


def fatorial(n):
    if n == 1 or n == 0 :
        return 1
    return n * fatorial(n-1)

def ehPar(n):
    if n%2 == 0:
        return True
    return False

def divideString(s):
    return(s.split(" "))

def inverso(n):
    s = str(n)
    return int(s[::-1])
