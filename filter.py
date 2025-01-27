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
#filtro de forma manual
novos_produtos = [
    p for p in produtos
    if p['preco'] > 10
]

print_iter(novos_produtos)

#Usando o Filter com lambda
produtos_filtrados = filter(
    lambda p:p['preco'] > 10,
    produtos 
)
#usando filter criando função
def acima_20(produto):
    return produto['preco'] > 20

prod_filter = filter(acima_20, produtos

)

print_iter(produtos_filtrados)

print_iter(prod_filter)