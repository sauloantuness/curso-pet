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

def divideString(a):
    b = a.split(" ")
    return b

def inverso(ent):
    string = str(ent)
    size = len(string)
    result = ""
    for i in range(size-1,-1,-1):
        result += string[i]
    return int(result)

def novoDict(nome,matricula,ehMulher):
    result = {
        'nome': nome,
        'matricula': matricula,
        'ehMulher': ehMulher
    }
    return result

def getNome(dictonary):
    return dictonary['nome']

def setNome(dictonary,nome):
    dictonary['nome'] = nome
    return dictonary

def setAulas(dictonary,aulas):

    d = {
        'aulas': aulas
    }
    dictonary.update(d)
    return dictonary

def insereAula(dictonary,aula):
    lista = []
    lista.append(aula)
    if not(dictonary.get('aulas')):
        dictonary['aulas'] = lista
    else:
        dictonary['aulas'].append(aula)
    return dictonary

def getAulas(dictonary):
    if not(dictonary.get('aulas')):
        return []
    return dictonary['aulas']

def quad(n):
    return n*n

def transforma(lista,func=quad):
    result = []
    for i in lista:
        result.append(func(i))
        
    return result
