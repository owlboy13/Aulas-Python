import json
import os

pessoas = [
    {
        "name": "Anderson",
        "lastname": "Luiz",
        "age": 30,
        "ativo": False,
        "notas": ['A', 'A+'],
        "Phone": {
            "residencial": "00 0000-0000",
            "celular": "00 0000-0000",
        },

        "address": [
            {"Street": "Rua Francisco leao Veloso"},
            {"City": "Uirauna"},
            {"State": "Paraíba"}
        ]
    },
    {
        "name": "Maria",
        "lastname": "Vieira",
        "age": 50,
        "ativo": False,
        "notas": ['B', 'C+'],
        "Phone": {
            "residencial": "00 0000-0000",
            "celular": "00 0000-0000",
        },
        "address": [
            {"Street": "Rua xxxxxxxxx"},
            {"City": "Uiraúna"},
            {"State": "Paraíba"}
        ]
    }
]

#Obtém o diretório atual onde o script está sendo executado
BASE_DIR = os.path.dirname(__file__)

# Define o caminho completo onde o arquivo JSON será salvo
# O arquivo será salvo no mesmo diretório do script, com o nome 'arquivo_python.json'
SAVE_TO = os.path.join(BASE_DIR, 'arquivo_python.json')

# Abre o arquivo no modo de escrita ('w') com codificação UTF-8
# O bloco 'with' garante que o arquivo será fechado automaticamente após o uso
with open(SAVE_TO, 'w+') as file:
    # Converte a lista 'pessoas' para o formato JSON e salva no arquivo
    # O parâmetro 'indent=2' formata o JSON com 2 espaços de indentação para melhor legibilidade
    json.dump(pessoas, file, ensure_ascii=False, indent=2)



# BASE_DIR = os.path.dirname(__file__)
# FILE_JSON = os.path.join(BASE_DIR, 'arquivo_python.json')

# with open(FILE_JSON, 'r+', encoding='utf-8') as file:
#     estrutura = json.load(file)
#     print(json.dumps(estrutura, indent=2))

#     # for estruturas in estrutura:
#     #     print(estruturas)