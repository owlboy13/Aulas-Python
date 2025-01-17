lista = [
    {'nome':'Anderson', 'sobrenome':'Luiz'},
    {'nome':'Maria','sobrenome':'das neves'},
    {'nome':'Genival','sobrenome':'Oliveira'},
]


# def exibir(lista):
#     for item in lista:
#         print(item)
#     print()

lista.sort(key=lambda item: item['nome'])
for nomes in lista:
    print(nomes)

def space_line():
    return print('=============================='),
print('==============================')


space_line()

def executa(funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x + y


print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
      executa(soma, 2, 3)
      )

