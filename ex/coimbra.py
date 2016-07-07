def fatorial(n):
	if(n == 0):
		return 1
	if(n == 1):
		return 1
	else:
		return n*fatorial(n-1)
def hi():
	return 'hi'
def ehPar(n):
	if(n%2 == 0):
		return True
	else:
		return False
def divideString(chave):
	lista = []
	for palavra in chave.split(' '):
		lista.append(palavra)	
	return lista

def inverso(chave):
	lista = []
	chave2 = ""
	chave_aux = str(chave)
	for letra in chave_aux:
		lista.append(letra)
	lista.reverse()
	for letra in lista:
		chave2 += letra
	return int(chave2)

def novoDict(nome,matricula,ehMulher):
	d = {
		'nome': nome,
		'matricula' : matricula,
		'ehMulher' : ehMulher,
	}
	return d

def getNome(d1):
	return d1['nome']

def setNome(d1,nome):
	d1['nome'] = nome
	return d1

def setAulas(d2,lista_aulas):
	d2['aulas'] = lista_aulas
	return d2

def insereAula(d3,aula):
	d3['aulas'].append(aula)
	return d3

def insereAula(d4,aula):
	if(d4.get('aulas')):
		d4['aulas'].append(aula)
	else:
		d4['aulas'] = [aula]
	return d4

def getAulas(d):
	if(d.get('aulas')):
		return d['aulas']
	else:
		return []

def quadrado(n):
	return n*n

def transforma(lista,funcao=quadrado):
	for i in range(0,len(lista)):
		lista[i] = funcao(lista[i])
	return lista
