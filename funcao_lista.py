def adicionar_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


clientes1 = adicionar_clientes('Anderson')
adicionar_clientes('Maria', clientes1)
clientes1.append('Genival')



clientes2 = adicionar_clientes('João')
adicionar_clientes('Joana', clientes2)
clientes2.append('hevila')


print(f'Lista de clientes 1: {clientes1}')
print(f'Lista de clientes 2: {clientes2}')
