#COUNT É UM ITERADOR SEM FIM (itertools)
from itertools import count


c1 = count(start=8, step=8) # com arguentos para soma
r1 = range(10)

#verificar se o metodo é iterator
print( 'c1', hasattr(c1, '__iter__'))

for i in c1:
    if i >= 100:
        break
    print(i)
print()

for r in r1:
    print(r)

