def hi():
    return 'hi'


def fatorial(n):
    if n == 1 or n == 0 :
        return 1
    return n * fatorial(n-1)

def ehPar(n):
    if n%2 == 0:
        return True
    return False

def divideString(s):
    return(s.split(" "))

def inverso(n):
    s = str(n)
    return int(s[::-1])

def getNome(d):
    return d.get('nome')

def novoDict(nome,matricula,ehMulher):
    d = {
        'nome': nome,
        'matricula': matricula,
        'ehMulher': ehMulher,
    }
    return d

def setNome(d,nome):
    d['nome']=nome
    return d

def setAulas(d,aulas):
    """novod2 = {
        'nome': 'Gabriela',
        'matricula': 2014123456,
        'ehMulher': False,
        'aulas': ['Fisica', 'Calculo']
    }"""
    d['aulas'] = aulas
    return d

def insereAula(d,aula):
    test = d.get("aulas",False)
    if test == False:
        d["aulas"] = [aula]
    else:
        d["aulas"].append(aula)
    return d

def getAulas(d):
    return d.get("aulas",[])
