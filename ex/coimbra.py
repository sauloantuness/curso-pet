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