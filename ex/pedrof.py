def hi():
    return "hi"

def fatorial(n):
    fatorial = 1
    for i in range (n,1,-1):
        fatorial*=i
    return fatorial

def ehPar(n):
    if n%2 == 0:
        return True
    else:
        return False

def divideString(string):
    s1 , s2 , s3 = string.split(" ")
    lista = [s1,s2,s3]
    return lista
