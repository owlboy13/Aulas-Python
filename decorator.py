#FUNÇÃO DECORADORA FEITO SEM USAR O @
def criar_funcao(fun):
    def interna(*args, **kwargs):
        print('Vou te decorar!')
        for arg in args:
            e_string(arg)
        result = fun(*args, **kwargs)
        print('Ok, agora voce foi decorado!')
        return result
    return interna


def inverte_strings(string):
    return string[::-1]

def e_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError('parametro deve ser uma string!')


invert_string_checando_parametro = criar_funcao(inverte_strings)
invertida = invert_string_checando_parametro('123')
print(invertida)

print()
print()

#FUNÇÃO DECORATOR COM @
def decoradora(func):
    def nova_funcao(*args, **kwargs):
        print('Vou decorar!')
        resultado = func(args, kwargs)
        print('decorado!')
        return resultado
    return nova_funcao

@decoradora #chamando função decorator
def teste(*args, **kwargs):
    produto = args
    valor = kwargs
    return produto, valor

v1 = teste('Feijão', valor=12)
print(v1)

print()
print()

#OUTRO EXEMPLO DE DECORATOR
def decorator(func):
    print('Decorador 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada

def soma(x,y):
    return x + y

multiplica = decorator(lambda x, y: x * y)

v2 = soma(10,20)
v3 = multiplica(10, 5)
print(v2)
print(v3)

print()
print()

# Unindo Listas com função ZIP
# def zipper(list1, list2):
#     new_list = list(zip(list1,list2))
#     return new_list

def zipper(l1, l2):
    new_list = min(len(l1), len(l2))
    return [(l1[i], l2[i]) for i in range(new_list)]


list1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']

list2 = ['BA', 'MG', 'SP', 'RJ']

new = zipper(list1,list2)
print(new)


#TESTANDO FUNÇÃO MAX
n1 = "Anderson"
n2 = "luiz"
max_list = max(len(n1), len(n2))
print(max_list)











