from functools import reduce

produtos = [
    {'nome':'Produto 5','preco':10.00},
    {'nome':'Produto 1','preco':22.32},
    {'nome':'Produto 3','preco':10.11},
    {'nome':'Produto 2','preco':105.87},
    {'nome':'Produto 4','preco':69.90},
]

# sem reduce
total = 0
for p in produtos:
    total = p['preco'] + total

print(f'R$ {round(total, 2)}')

# list compreehension
print(round(sum([p['preco'] for p in produtos])),2)


# reduce  - faz a redução de um iteravel em um valor
def funcao_do_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto',produto)
    total = acumulador + produto['preco']
    print('R$',round(total,2))
    return total

v1 = reduce(
    funcao_do_reduce,
    produtos,
    0
)