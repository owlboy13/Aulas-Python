from functools import partial

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome':'Produto 5','preco':10.00},
    {'nome':'Produto 1','preco':22.32},
    {'nome':'Produto 3','preco':10.11},
    {'nome':'Produto 2','preco':105.87},
    {'nome':'Produto 4','preco':69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

def ordena(lista):
    return sorted(lista)

# não será preciso passar o parametro para função
aumentar_dez = partial(
    aumentar_porcentagem, 
    porcentagem=1.1)


#list comprehension
novos_produtos = [
    {**p,
     'preco': aumentar_dez(p['preco'])}
    for p in produtos
]

#ordenando dados
produtos_ordenados = sorted(novos_produtos, key=lambda x:x['preco'], reverse=True)


def mudar_preco(produto):
    return {
        **produto, 'preco': aumentar_dez(produto['preco'])
    }

#irá iterar por cada item da lista e usar a função para alterar o valor
produto_alterado = map(mudar_preco, produtos)

print_iter(produto_alterado)
print_iter(produtos)
print_iter(produtos_ordenados)
 
 # Verificar se é iteravel
print(hasattr(produto_alterado, '__iter__'))

# outra forma de se usar o map com a função lambda
print(list(map(
    lambda x:x *3,
    [1,2,3,4]
    ))
)