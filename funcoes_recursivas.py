'''
CASO QUEIRA PASSAR O LIMITE DE RECURSÃO 

import sys

sys.setrecursionlimit(1000) <- parametro que deseja alcançar


'''


def recursiva(start=0, end=10):
    if start >= end:
        return end
    start += 1
    return recursiva(start, end)


print(recursiva())

def fatorial(n):
    if n <= 0 or n <= 1:
        return 1 
    else:
        return n * fatorial(n-1)
    
print(fatorial(5))


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(10))

