# exercício 1

vendas = [1500, 2000, 800, 3500, 1200]


total = sum(vendas)
media_vendas = total / len(vendas)
melhor_venda = max(vendas)
pior_venda = min(vendas)

print(f'{total:,.2f}')
print(f'{media_vendas:,.2f}')
print(f'{melhor_venda:,.2f}')
print(f'{pior_venda:,.2f}')

# exercício 2

estoque = ['monitor', 'teclado', 'mouse', 'headset']

estoque.append('webcam')

teclado = estoque.index('teclado')
estoque[teclado] = 'teclado mecanico'
    
estoque.pop(2)

print(estoque)
print('impressora' in estoque)

# exercício 3

fretes = [50, 80, 20, 150, 40]
fretes.sort()

fretes.sort(reverse=True)
top_fretes = fretes[:2]

print(f'Lista original: {fretes}, top fretes: {top_fretes}')

# exercício 4

rota = ['São Paulo', 'Campinas', 'Jundiai', 'Sorocaba']
novas_cidades = ['Itu', 'Valinhos']

rota.extend(novas_cidades)

posicao = rota.index('Sorocaba')

print(rota, posicao)
print(f'Sorocaba é a {posicao}° cidade da rota')

# exercício 5

precos = [100.0, 250.0, 500.0]
vinhos = ['Branco', 'Tinto', 'Champagne']

produto = input('Digite o nome do produto: ')
novo_preco = float(input('Digite o novo preço do produto: '))

posicao = vinhos.index(produto)
precos[posicao] = novo_preco

print(f'Nomes: {vinhos}')
print(f'Preços: {precos}')