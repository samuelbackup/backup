# exercício 1

faturamento = 45000
custo = 23500

lucro = faturamento - custo
margem_lucro = lucro / faturamento
print(f'O lucro da empresa foi de R${lucro:,.2f}, e a margem de lucro de {margem_lucro:.2%}')

# exercício 2

nome = ' mArCoS aNtOnIo rOcHa '
email = ' MARCOS.ROCHA@GMAIL.COM '

nome = nome.strip()
email = email.strip()

nome = nome.title()
email = email.lower()

print(nome)
print(email)

# exercício 3

email = 'andre_silva@empresa.com.br'
novo_email = email.replace('empresa.com.br', 'grupocorp.com')
print(novo_email)

# exercício 4

email = 'beatriz.oliveira@grupocorp.com'
posicao_arroba = email.find('@')
nome = email[:posicao_arroba]

# print(nome)

# exercício 5

nome = 'lucas ferreire sousa'
primeiro_espaco = nome.find(' ')
print(primeiro_espaco)
primeiro_nome = nome[:primeiro_espaco]
primeiro_nome = primeiro_nome.capitalize()
print(f'Olá, {primeiro_nome}, seja bem-vindo ao nosso clube!')
