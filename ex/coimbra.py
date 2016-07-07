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
