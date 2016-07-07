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
    
def inverso(num):
	return int(str(num)[::-1])

def novoDict(nome,matricula,ehMulher):
	l={}
	l['nome'] = nome
	l['matricula']=matricula
	l['ehMulher']=ehMulher
	return l
	
print (novoDict('Higorf', 2014123456, False))
