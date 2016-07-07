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

def divideString (string):

    s1 , s2, s3 = string.split(' ')
    l=[s1,s2,s3]
    return l

def inverso (numero):
    return int(str(numero)[::-1])

def novoDict(gnome,gmatricula,gehMulher):
    aux={
        "nome": gnome,
        "matricula" :gmatricula,
        "ehMulher" : gehMulher
    }
    return aux

def getNome(dicts):
    return dicts['nome']

def setNome(dicts,gnome):
    dicts['nome']=gnome
    return dicts

def setAulas(dicts,gaulas):
    aux={
        "nome": dicts['nome'],
        "matricula" :dicts['matricula'],
        "ehMulher" : dicts['ehMulher'],
        "aulas" : gaulas

    }
    return aux

def insereAula(dicts,naula):
    if dicts.get("aulas"):
        dicts["aulas"].append(naula)
    else:
        dicts["aulas"]=[naula]
    return dicts

def getAulas(dicts):
    if dicts.get("aulas"):
        return dicts["aulas"]
    else:
        return []
