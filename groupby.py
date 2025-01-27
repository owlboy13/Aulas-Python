from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 10},
    {'nome': 'Anderson', 'nota': 7},
    {'nome': 'Maria', 'nota': 5},
    {'nome': 'Hevila', 'nota': 5},
    {'nome': 'Pedro', 'nota': 10},
    {'nome': 'Do carmo', 'nota': 7},
]

def ordena(aluno):
    return aluno['nota']


print(*alunos, sep='\n')

#printando apenas as notas
for i in alunos:
    print(i['nota'])
print()

# ordenando lista
grupos = sorted(alunos, key=ordena)
for aluno in grupos:
    print(aluno)

print()

#Agrupando alunos por nota
agrupamento = groupby(grupos, key=ordena)
for chave, grupo in agrupamento:
    print(chave)
    print(list(grupo))
