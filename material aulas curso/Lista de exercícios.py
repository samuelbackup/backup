# Nível 1 - Básico (Entrada, Saída e Variáveis)
# 1
# nome = input('Digite o seu nome: ')
# print(f'Seja bem-vindo {nome}!')

# # 2
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# s = n1 + n2
# print(f'{s}')

# 3
# idade = int(input('Informe sua idade: '))
# print(f'{2026 - idade}')

# 4
# numero = float(input('Digite um número: '))
# dobro = numero * 2
# triplo = numero * 3
# print(f'O dobro do número {numero} é {dobro} e o seu triplo é {triplo}')

# 5
# valor = float(input('Informe quantos reais você tem: R$'))
# print(f'{valor:.2f}')

# Nível 2 - Condições (if, else, elif)
# 6
# numero = int(input('Digite um número: '))
# if numero >= 0:
#     print('Número positivo')
# else:
#     print('Número negativo')

# 7
# idade = int(input('Digite sua idade: '))
# if idade >= 18:
#     print('Maior de idade')
# else:
#     print('Menor de idade')

# 8
# nota = float(input('Digite sua nota: '))
# if nota >= 7:
#     print('Aprovado')
# else:
#     print('Reprovado')

# 9
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# n3 = int(input('Digite mais um número: '))
# if n1 > n2 and n1 > n3:
#     print(f'{n1} é o maior número')
# elif n2 > n3:
#     print(f'{n2} é o maior número')
# else:
#     print(f'{n3} é o maior número')

# 10
# nota = float(input('Digite sua nota: '))
# if nota >= 8.5:
#     print('Excelente')
# elif nota >= 7:
#     print('Bom')
# elif nota == 6:
#     print('Regular')
# else:
#     print('Ruim')

# Nível 3 - Laços de repetição (while e for)
# 11
# for i in range(1, 11):
#     print(i)

# 12
# soma = 0
# for i in range(5):
#     numero = float(input(f'Digite o {i+1}° número: '))
#     soma += numero
# print(f'A soma é {soma}')

# 13
# for i in range(1, 101):
#     print(i)

# 14
# while True:
#     numero = float(input('Digite um número: '))
#     if numero == 0:
#         break
#     print(f'Você digitou {numero}')
# print('Programa encerrado')

# 15
# senha = ''
# while senha != '1234':
#     senha = input('Digite a senha: ')
# print('Acesso Liberado')

# Nível 4 - while True (validação e controle)
# 16
# while True:
#     idade = int(input('Digite sua idade: '))
#     if idade > 0:
#         break
#     print('Idade inválida, tente novamente')
# print(f'Idade cadastrada: {idade}')

# 17
# while True:
#     print('1 - Opção 1')
#     print('2 - Opção 2')
#     print('3 - Sair')
#     opcao = input('Esolha uma opção: ')
#     if opcao == '1':
#         print('Você escolheu a opção 1')
#     elif opcao == '2':
#         print('Você escolheu a opção 2')
#     elif opcao == '3':
#         print('Saindo...')
#         break
#     else:
#         print('Opção inválida, tente novamente')

# 18
# while True:
#     numero = float(input('Digite um número: '))
#     if numero > 0:
#         break
#     print('Número inválido')
# print(f'Número {numero} é válido')

# 19
# senha_correta = '1234'
# while True:
#     senha = input('Digite sua senha: ')
#     if senha == senha_correta:
#         print('Acesso liberado')
#         break
#     print('Senha incorreta, tente novamente')

# 20
# nomes = []
# while True:
#     nome = input('Digite um nome: ')
#     if nome == 'fim':
#         break
#     nomes.append(nome)
#     print(nome)
# print(f'Nomes cadastrados: {nomes}')

# Nível 5 - Strings e Manipulação
# 21
# palavra = 'onomatopeia'
# palavra = len(palavra)
# print(palavra)

# 22
# a = 'cachorro'
# inverso = a[::-1]
# print(inverso)

# 23
# a = 'paralelepipedo'
# print(a.count('e'))

# 24
# palavra = input("Digite uma palavra: ")
# if palavra == palavra[::-1]:
#     print(f'"{palavra}" é um palíndromo')
# else:
#     print(f'"{palavra}" não é um palíndromo')

# 25
# frase = input('Digite uma frase: ')
# palavras = frase.split()
# print(palavras)

# Nível 6 - Desafios Avançados
# 26
# notas = [6, 8, 3, 4.8, 7.2, 8.3]
# media = sum(notas) / len(notas)
# print(f'Média: {media:.2f}')
# if media >= 7:
#     print('Aprovado')
# elif media > 4:
#     print('Recuperação')
# else:
#     print('Reprovado')

# notas = []
# for nota in range(6):
#     nota = float(input(f'Digite a {nota+1}° nota: '))
#     notas.append(nota)
# media = sum(notas) / len(notas)
# print(f'Média: {media:.2f}')
# if media >= 7:
#     print('Aprovado')
# elif media > 4:
#     print('Recuperação')
# else:
#     print('Reprovado')

# 27
