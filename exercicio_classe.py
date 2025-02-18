'''
Exercicio - Salve sua classe em json
Salve os dados da sua classe em json
e depois crie novamente as instâncias da classe com os dados salvos
arquivos separados
'''
import json
import os   


dados = {
    'nome': 'Anderson',
    'sobrenome': 'Luiz',
    'idade': 30,
    'peso': 80,
    'sexo': 'as vezes'
}

class Cadastro:
    def __init__(self, nome, sobrenome, idade, peso, sexo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.peso = peso
        self.sexo = sexo

    def exibir(self):
        print(self.__dict__)


c1 = Cadastro(**dados)

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'dados_classe.json')
def in_dump():
    with open(SAVE_TO, 'w+', encoding='utf-8') as arquivo:
        json.dump(c1.__dict__, arquivo, indent=2 , ensure_ascii=False)
        print("Arquivo JSON criado")
        print(c1.__dict__)

if __name__ == "__main__":
    in_dump()