class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Anderson', 'Luiz')
print(p1.nome,p1.sobrenome)


class Carro:
    #atributos
    def __init__(self, nome, cor, motor):
        self.nome = nome
        self.cor = cor
        self.motor = motor
        print(f'{self.nome} - Cor: {self.cor} - Motor: {self.motor}')


    #método
    def acao(self, numero):
        self.numero = numero
        count = 0
        while count < self.numero:
            for i in range(self.numero):

                count += 1 
                print(f'O {self.nome} deu a {count}ª volta')       
        else:
            print(f'O {self.nome} Parou...')
            print()

    def executar(self, *args, **kwargs):
        self.acao(*args, **kwargs)



carro_01 = Carro("Opala", "preto", 2.0)
carro_01.acao(15)

carro_02 = Carro("Brasilia", "Amarela", 1.0)
carro_02.acao(10)


print()

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def fotografar(self):
        if self.filmando == True:
            print(f'{self.nome} não pode fotografar pois está filmando...')
        else:
            print(f'{self.nome} está fotografando...')

    def parar_filmar(self):
        print(f'{self.nome} parando de filmar...')
        self.filmando = False
    
        


c1 = Camera('Sony')
c2 = Camera('Canon')

c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Anderson', 32)


print(p1.get_ano_nascimento())
print()
p1.__dict__['nome'] = 'Maria'
p1.__dict__['peso'] = 80
print(p1.__dict__)
print()
print(vars(p1))

print()
dados = {'nome': 'Raimundo','idade': 35}

p2 = Pessoa(**dados)
print(p2.__dict__)
p2.__dict__['peso'] = 90
print(p2.__dict__)

        
        



