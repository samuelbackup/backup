alunos = []

def cadastrar_aluno():
    nome = input('\nNome: ')
    while nome == '':
        print('Esse espaço não pode ficar vazio!')
        nome = input('Nome: ')
    idade = input('Idade: ')
    
    while not idade.isdigit():
        print('Digite apenas números!')
        idade = input('Idade: ')
    turma = input('Turma: ')
    aluno = {
        'Nome': nome,
        'Idade': idade,
        'Turma': turma
    }
    alunos.append(aluno)
    print('Aluno cadastrado com sucesso!')
    
def listar_alunos():
    for aluno in alunos:
        print('-----------')
        for chave, valor in aluno.items():
            print(f'{chave}: {valor}')
            
def buscar_aluno():
    nome = input('Nome do aluno: ')
    for aluno in alunos:
        print('------------')
        if aluno['Nome'].lower() == nome.lower():
            for chave, valor in aluno.items():
                print(f'{chave}: {valor}')
            return
            
while True:
    print('\n1 - Cadastrar')
    print('2 - Listar alunos')
    print('3 - Buscar aluno')
    print('4 sair')
    
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        cadastrar_aluno()
    elif opcao == '2':
        listar_alunos()
    elif opcao == '3':
        buscar_aluno()
    elif opcao == '4':
        print('Saindo...')
        break
    else:
        print('Opção inválida!')
