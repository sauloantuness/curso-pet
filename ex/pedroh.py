def hi():
    return "hi"

def fatorial(num):
    result = 1
    if num == 0:
        return 1
    else:
        for i in range(1,num + 1):
            result *= i
        return result

def ehPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

def divideString(st):
    return st.split(" ")

def inverso(intInput):
    strString = str(intInput)
    strNova = ""
    for i in range(len(strString) -1 ,-1,-1):
        strNova += strString[i]
    return int(strNova)

def novoDict(strString,intNum,boolBo):
    return {
        'nome': strString,
        'matricula': intNum,
        'ehMulher': boolBo
    }

def getNome(d1):
    return d1['nome']

def setNome(d1, newName):
    d1['nome'] = newName
    return d1

def setAulas(d2, listAulas):
    d2['aulas'] = []
    for aula in listAulas:
        d2['aulas'].append(aula)
    return d2

def insereAula(d3, newAula):
    if d3.get('aulas'):
        d3['aulas'].append(newAula)
    else:
        listAulas = [newAula]
        setAulas(d3,listAulas)
    return d3

def getAulas(d4):
    if d4.get('aulas'):
        return d4['aulas']
    else:
        return []

def quadrado(n):
    return n*n

def transforma(listNumbers, func = quadrado ):
    newList = []
    for num in listNumbers:
        newList.append(func(num))
    return newList

if __name__ == "__main__":
    num = int(input())
    print(test_inverso(num))
