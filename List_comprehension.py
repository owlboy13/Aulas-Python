produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.98},
]

for i in produtos:
    print(i)

print()

novos_produtos = [
    
    {**produto, 'preco': round(produto['preco'] + 10/100, 2)}
    if produto['preco'] > 0 else {**produto}
    for produto in produtos
]

# produtos_ordenados = sorted(novos_produtos, key=lambda dicionario: dicionario['preco'])
produtos_ordenados = sorted(novos_produtos, key=lambda dicionario: dicionario['nome'])
print(*produtos_ordenados, sep='\n')

'''
SINTAXE BÁSICA
# [expressão for item in teravel if conclucao]

** <- desempacotamento de dict, exemplo (**nome_dict)
'''

