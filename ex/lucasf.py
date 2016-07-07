def hi():
    return "hi"

def fatorial (num):
    fat=1
    while num>0:
        fat=fat*num
        num=num-1
    return fat

def ehPar (num):
    if (num%2==0):
        return 1
    else:
        return 0

def lista (string):

    s1 , s2, s3 = string.split(' ')
    l=[s1,s2,s3]
    return l

def inverso (numero):
    return int(str(numero)[::-1])
