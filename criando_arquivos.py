''' 
Criando Arquivos com Python
r - leitura
w - escrita
x - criação
a - escreve ao final
b - binario
t - modo texto
+ - leitura e escrita

Context manager - with (abre e fecha)

'''
import os 
caminho_arquivo = r'C:\Users\Anderson Luiz\Downloads\Anderson - Importante\Projetos de Programação\Aulas Python\new_name.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Ola mundo\n')
#     arquivo.write('segunda linha\n')
#     print('arquivo fechado')

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

# with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
#     arquivo.write('atenção\n')

# new_name = os.rename(caminho_arquivo, 'new_name')
# print('Arquivo renomeado')


file_delete = os.remove(caminho_arquivo)
if file_delete == None:
    print('deletado')



