#FUNÇÃO DECORADORA
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





