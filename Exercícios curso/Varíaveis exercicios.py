# exercício 1

faturamento_inicial = 50000
percentual_bonus = 0.1
bonus = faturamento_inicial * percentual_bonus

faturamento_total = faturamento_inicial - bonus

print(faturamento_total)

# exercício 2

smartphones_estoque = 250
print(smartphones_estoque)

vendas = 78
smartphones_estoque = smartphones_estoque - vendas
print(smartphones_estoque)

smartphones_estoque = smartphones_estoque + 100
estoque_fim = smartphones_estoque
print(estoque_fim)

# exercício 3

caixas = 1250
caminhao_suporta = 12
caminhoes_cheios = caixas // caminhao_suporta
print(caminhoes_cheios)

cargas_sobrando = caixas % caminhao_suporta
print(cargas_sobrando)

# exercício 4

faturamento = 15000
custos_fixos = 5000
imposto_percentual = 0.15

imposto = faturamento * imposto_percentual
lucro_liquido = faturamento - custos_fixos - imposto
margem_lucro = lucro_liquido / faturamento

meta_atingida = bool(margem_lucro > 0.30)

print(f'{imposto:.2f}')
print(f'{lucro_liquido:.2f}')
print(f'{margem_lucro:.2%}')
print(meta_atingida)

# exercício 5

meses = 40 # meses
anos = 40 // 12
meses_restantes = 40 % 12
print(f'{anos} anos e {meses} meses')