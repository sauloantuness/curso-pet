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
	
def getNome(d1):
	return d1['nome']

def setNome(d1,nome):
	d1['nome'] = nome
	return d1
	
def setAulas(d2, l):
	d2['aulas'] = l
	return d2

def insereAula(d3,aula):
	if d3.get('aulas',None) == None :
		d3['aulas'] = [aula]
	else :
		d3['aulas'].append(aula)
	return d3
	
def getAulas(d4):
	if d4.get('aulas',None) != None:
		return d4['aulas']
	return []
