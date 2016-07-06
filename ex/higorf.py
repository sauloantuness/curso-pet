def hi():
    return 'hi'

def fatorial(num):
    i = 1
    while num > 0:
        i *= num
        num-=1
    return i

def ehPar(num):
    if num % 2 == 0 :
        return True
    return False

def divideString(string):
    l = []
    l.append(string.split(' '))
    return l[0]
