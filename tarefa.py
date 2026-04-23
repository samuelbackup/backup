tarefas = []

while True:
    print('Área de tarefas\n')
    print('Digite 1 para adicionar uma tarefa')
    print('Digite 2 para listar as tarefas')
    print('Digite 0 para sair')
    
    opcao = input('\nEscolha uma opção: ')
    
    if opcao == '0':
        print('Saindo...')
        break
    elif opcao == '1':
        tarefa = input('Adicione uma tarefa: ')
        tarefas.append(tarefa)
        print('Tarefa adicionada')
    elif opcao == '2':
        print('\n--- Lista de tarefas ---')
        for tarefa in tarefas:
            print(tarefa)
    else:
        print('Opção inválida')