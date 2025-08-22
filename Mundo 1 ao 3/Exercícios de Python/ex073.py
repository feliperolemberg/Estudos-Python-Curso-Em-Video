times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Bragantino', 'Fluminense',
         'Ceará', 'Bahia', 'Corinthians', 'Mirassol', 'Atlético-MG',
         'Botafogo', 'Grêmio', 'São Paulo', 'Internacional', 'Vasco',
         'Fortaleza', 'Vitória', 'Santos', 'Juventude', 'Sport')
print(f'Os 5 primeiros colocados do Brasileirão Serie A 2025 atualmente são:')
for c in range(0,5):
    print(f'{c+1}º - {times[c]}')
print('-=-' * 10)
print('Os últimos 4 colocados são:')
for c in range(16, 20):
    print(f'{c+1}º - {times[c]}')
print('-=-' * 10)
print('Os times em ordem alfabética:')
for c in range(0,20):
    timesalfa = sorted(times)
    print(f'{timesalfa[c]}', end=', ' if c < 19 else '.\n')
print('-=-' * 10)
print(f'O Sport está na {times.index('Sport') + 1}ª posição.')
