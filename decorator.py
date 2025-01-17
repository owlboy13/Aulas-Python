def criar_funcao(fun):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        result = fun(*args, **kwargs)
        return result
    return interna

def inverte_strings(string):
    return string[::-1]

def e_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError('parametro deve ser uma string')



invert_string_checando_parametro = criar_funcao(inverte_strings)
invertida = invert_string_checando_parametro('123')
print(invertida)




