def hi():
    return 'hi'

def fatorial(n):
   if n<=1:
      return 1
   else:
      return n*fatorial(n-1)

def ehPar(n):
    if (n%2) == 0:
        return True
    else:
        return False

def divideString(s):
    return s.split()
