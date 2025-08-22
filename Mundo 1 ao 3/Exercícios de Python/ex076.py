listagem = ('Pão francês', 0.50, 'Leite', 5,
            'Pão de forma', 8, 'Iogurte', 6,
            'Caneta', 1, 'Guaramix', 1.5,
            'Barra de cereal', 1.75)
print('-=-' * 12)
print(f'{'LISTAGEM DE PREÇOS':^36}')
print('-=-' * 12)
for c in range(len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<28}', end='')
    else:
        print(f'R$ {listagem[c]:.2f}')
print('-=-' * 12)
