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

if __name__ == "__main__":
    num = int(input())
    print(fatorial(num))
    print(ehPar(num))
