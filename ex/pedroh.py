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


if __name__ == "__main__":
    num = int(input())
    print(fatorial(num))
