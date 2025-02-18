import json
import os
from exercicio_classe import Cadastro, in_dump

CAMINHO = './dados_classe_2.json'

with open('dados_classe.json', 'r+') as file:
    file_save = json.load(file)

c2 = Cadastro(**file_save)
c2.__dict__['nome'] = 'Raimundo'
c2.__dict__['sobrenome'] = 'Ferreira'
c2.__dict__['idade'] = 80
c2.__dict__['peso'] = 100
c2.__dict__['sexo'] = 'nunca'
c2.__dict__['Estado Civil'] = 'Casado'


with open('dados_classe_2.json', 'w+') as file2:
    json.dump(c2.__dict__, file2, ensure_ascii=False, indent=2)
    print("Novo arquivo JSON criado")
    print()
    print(c2.__dict__)

