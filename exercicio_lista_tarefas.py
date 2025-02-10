# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import json
import os

def main():
    lista_total = []    

    lista_deletados = []

    # Função para listar tarefas
    def print_list(lista):
        if lista_total == []:
            print('Nenhuma Tarefa para o dia de hoje')
        else:
            for listas in lista:
                print(f'\t\t{listas}')
            print()

    #Função para Adicionar Tarefas a lista
    def adicionar_tarefa(tarefa):
        tarefa = tarefa.strip()
        lista_total.append(tarefa)
        print_list(lista_total)
        return lista_total
    
    # Função para deletar última tarefa adicionada
    def deletar_tarefa():
        if lista_total == []:
            print('Não tem o que desfazer')
        else:
            deletado = lista_total.pop()
            lista_deletados.append(deletado)
            print_list(lista_total)
            return lista_total
    
    def refazer():
        if lista_deletados == []:
            print('Não tem mais o que refazer')
            print()
            pass
        else:
            lista_total.append(lista_deletados[-1])
            lista_deletados.pop()
            print_list(lista_total)



    # Laço While para manter programa funcionando sem fechar
    while True:
        print()
        print('Comandos: Listar, Desfazer, Refazer ou Sair')

        tarefa = input('Digite uma tarefa ou comando:  ').lower()
        print('Lista de Tarefas:')

        comandos = {
            'listar': lambda: print_list(lista_total),
            'desfazer': lambda: deletar_tarefa(),
            'refazer': lambda: refazer(),
            'limpar': lambda: main(),
            'adicionar': lambda: adicionar_tarefa(tarefa),
        }

        if tarefa == 'sair':
            print('Programa Encerrado')
            break

        comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']

        comando()


        BASE_DIR = os.path.dirname(__file__)
        SAVE_TO = os.path.join(BASE_DIR, 'Lista_Tarefas.json')

        with open(SAVE_TO, 'w+', encoding='utf-8') as arquivo:
            json.dump(lista_total, arquivo, indent=2)

        # tarefa = input('Digite uma tarefa ou comando:  ').lower()
        # print('Lista de Tarefas:')
        
        # if tarefa == 'limpar':
        #     print('Limpando toda lista')
        #     main()

        # elif tarefa == 'sair':

        # elif tarefa == 'listar':
        #     print_list(lista_total)

        # elif tarefa == 'desfazer':
        #     deletar_tarefa()

        # elif tarefa == 'refazer':
 ,
        # else:
        #     # Condição para adicionar tarefa
        #     adicionar_tarefa(tarefa)
            
if __name__ == '__main__':
    main()