candidato1 = 0
candidato2 = 0
candidato3 = 0

while True:
    print('\n1 - Candidato 1')
    print('2 - Candidato 2')
    print('3 - Candidato 3')
    print('0 - Encerrar votação')
    
    voto = input('Vote no seu candidato: ')
    
    if voto == '0':
        break
    elif voto == '1':
        candidato1 += 1
        print('Voto computado')
    elif voto == '2':
        candidato2 += 1
        print('Voto computado')
    elif voto == '3':
        candidato3 += 1
        print('Voto compuado')
    else:
        print('Voto inválido')
    
total = candidato1 + candidato2 + candidato3
    
print('\n--- Resultado da votação ---')
print(f'Candidato 1: {candidato1} votos')
print(f'Candidato 2: {candidato2} votos')
print(f'Candidato 3: {candidato3} votos')

if total == 0:
    print('Nenhum voto foi computado')
elif candidato1 == candidato2 == candidato3:
    print('Empatate entre todos os candidatos')
elif candidato1 == candidato2 > candidato3:
    print('Empate entre Candidato 1 e Candidato 2')
elif candidato1 == candidato3 > candidato2:
    print('Emptate entre Candidato 1 e Candidato 3')
elif candidato2 == candidato3 > candidato1:
    print('Empate entre Candidato 2 e Candidato 3')
elif candidato1 > candidato2 and candidato1 > candidato3:
    print('Vencedor: Candidato 1')
elif candidato2 > candidato3:
    print('Vencedor: Candidato 2')
else:
    print('Vencedor: Candidato 3')