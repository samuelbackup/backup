# exercício 1

valor_bruto = input('Digite o valor bruto: R$')

valor_bruto = valor_bruto.replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')

valor_bruto = float(valor_bruto)

imposto = valor_bruto * 0.15

print(f'O valor do imposto é R$ {imposto:.2f}')

# exercício 2

nome_completo = input('Digite o seu nome completo: ')
email_colaborador = input('Digite seu email: ')

primeiro_nome = nome_completo.split()[0].capitalize()
email_colaborador = email_colaborador.strip().lower()
print(f'Cadastro concluído: {primeiro_nome}. E-mail de acesso: {email_colaborador}')

# exercício 3

loja_a = float(input('Faturamento da Loja A: '))
loja_b = float(input('Faturamento da Loja B: '))

faturamento_total = loja_a + loja_b

media_faturamento = faturamento_total / 2

print(f'O total de faturamento das duas lojas foi R${faturamento_total:,.2f}, e a média foi de R${media_faturamento:,.2f}')