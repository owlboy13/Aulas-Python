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

def main():
    lista_total = []    

    lista_deletados = []

    # Função para listar tarefas
    def print_list(lista):
        for listas in lista:
            print(listas)
        print()

    #Função para Adicionar Tarefas a lista
    def adicionar_tarefa(tarefa):
        lista_total.append(tarefa)
        return lista_total
    
    # Função para deletar última tarefa adicionada
    def deletar_tarefa():
        deletado = lista_total.pop()
        lista_deletados.append(deletado)
        return lista_total

    # Laço While para manter programa funcionando sem fechar
    while True:
        print()
        print('Comandos: Listar, Desfazer, Refazer ou Sair')

        if lista_total == []:
            print('Nenhuma Tarefa para o dia de hoje')
        else:
            print('Lista de Tarefas:')
            print_list(lista_total)

        tarefa = input('Digite uma tarefa ou comando:  ').lower()
        print('Lista de Tarefas:')
        
        if tarefa == 'limpar':
            print('Limpando toda lista')
            main()

        elif tarefa == 'sair':
            print('Encerrando o Programa...')
            break
        elif tarefa == 'listar':
            print_list(lista_total)

        elif tarefa == 'desfazer':
            deletar_tarefa()

        elif tarefa == 'refazer':
            lista_total.append(lista_deletados[-1])
            lista_deletados.pop()

        else:
            # Condição para adicionar tarefa
            adicionar_tarefa(tarefa)
            
if __name__ == '__main__':
    main()