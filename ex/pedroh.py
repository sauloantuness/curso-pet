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

if __name__ == "__main__":
    num = int(input())
    print(test_inverso(num))
