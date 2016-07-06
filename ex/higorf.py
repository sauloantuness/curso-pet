def hi():
    return 'hi'

def fatorial(num):
    i = num - 1
    while i > 0:
        num *= i
        i-=1
    return num

print(fatorial(0))
