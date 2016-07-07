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

def inverso(n):
    return int(str(n)[::-1])

def novoDict(nome, matricula, ehMulher):
    d = {}
    d["nome"] = nome
    d["matricula"] = matricula
    d["ehMulher"] = ehMulher
    return d

def getNome(d):
    return d.get("nome")

def setNome(d, nome):
    d["nome"] = nome
    return d

def setAulas(d, aulas):
    d["aulas"] = aulas
    return d

def insereAula(d, aula):
    if d.get("aulas"):
        d["aulas"].append(aula)
    else:
        d["aulas"] = [aula]
    return d

def getAulas(d):
    if d.get("aulas"):
        return d.get("aulas")
    return []
