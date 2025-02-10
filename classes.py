class Vendedor:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def meta(self, meta):
        if self.vendas >= meta:
            print(self.nome, "bateu a meta")
        else:
            print(self.nome, "Não bateu a meta")

vendedor1 = Vendedor("Anderson")
vendedor1.vendeu(800)
vendedor1.meta(500)

vendedor2 = Vendedor("Luiz")
vendedor2.vendeu(400)
vendedor2.meta(500)


print()
print()

#Metodos em instancias de classes python

class Carros:
    def __init__(self, nome = 'sei lá' ):
        self.nome = nome

    def valor(self, valor):
        self.valor = valor
        print(self.nome, self.valor)

    def ano(self, ano):
        self.ano = ano
        print(self.nome, self.valor, self.ano)
    
    def motor(self, motor):
        self.motor = motor
        print(self.nome, self.motor, self.ano, self.valor)



carro = Carros('Celta')

valor_carro = carro.valor(10000)

ano_carro = carro.ano(2008)

motor_carro = carro.motor(1.0)

print()
print()

class Animal:
    def __init__(self, nome):
        self.nome = nome


    def comendo(self, alimento):
        return f'{self.nome} está comendo um {alimento}'


animal1 = Animal('Leão')
alimento1 = animal1.comendo('Veado')
print(alimento1)

print()
print()

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
           print(f'{self.nome} está filmando...')
           self.filmando = True

cannon = Camera('Sony')

cannon.filmar()

# DESCOBRINDO ANO DE NASCIMENTO
class Pessoa:
    ano_atual = 2024
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_anodenascimento(self):
        return self.ano_atual - self.idade
    
p1 = Pessoa('Anderson', 31)
p2 = Pessoa('Hevila', 29)
print(p1.get_anodenascimento())
print(p2.get_anodenascimento())


class Boneco:
    def __init__(self, nome):
        self.nome = nome




