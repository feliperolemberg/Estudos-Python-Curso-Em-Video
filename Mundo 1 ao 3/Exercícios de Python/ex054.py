from datetime import date
print('Digite o ano de nascimento de 7 pessoas.')
contador = 0
for c in range(0, 7):
    anonasc = int(input('Ano de nascimento: '))
    if date.today().year - anonasc >= 21:
        contador += 1
print('Das 7 pessoas cadastradas, {} são/serão maiores de idade em {}, e {} não são.'.format(contador, date.today().year, 7-contador))
