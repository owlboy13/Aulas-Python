﻿
pergunta_1 =  [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
print()
print('Responda as perguntas!')
print()

qtd_acertos = 0
for questao in pergunta_1:
    print('Pergunta:',questao['Pergunta'])
    print()

    opcoes = (questao['Opções'])
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)      
    print()

    escolha = input('Escolha uma das alternativas: ')

    acertou = False
    qtd_opcoes = len(opcoes)
    escolha_int = None

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == questao['Resposta']:
                acertou = True
    
    if acertou:
        qtd_acertos += 1
        print('Acertou 👌 ')
    else:
        print('Errou 👎 ')

print()

print('Você acertou', qtd_acertos)
print('de', len(pergunta_1), 'perguntas.')
