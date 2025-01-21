# Combinatios, Permutations e Product - itertools

from itertools import combinations, permutations, product

pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia',
]

camisetas = [
    ['preta', 'branca'],
    ['p','m',],
    ['masculino','feminino','unissex'],
    ['algodão','poliéster']
]

# chama a lista e o insere o numero de grupos 
# que deseja combinar
new_list = list(combinations(pessoas, 2))
list_perm = list(permutations(pessoas, 2))
# precisa desempacotar para combinar os produtos
lista_camisas = list(product(*camisetas)) 

for i in new_list:
    print(i)

print()

for r in list_perm:
    print(r)

print()

for c in lista_camisas:
    print(c)

