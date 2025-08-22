from math import trunc
num = int(input('Digite um número de 0 a 9999: '))
um = int(num/1000)
cen = int(num/100) - (um*10)
dez = int(num/10) - ((um*100) + (cen*10))
uni = num - ((um*1000) + (cen*100) + (dez*10))
print('Quantidade de unidades de milhar: {}'.format(um))
print('Algarismo das centenas: {}'.format(cen))
print('Algarismo das dezenas: {}'.format(dez))
print('Algarismo das unidades: {}'.format(uni))

''' u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10
Na operação de resto da divisão por 10 conseguimos sempre extrair o algarismo das unidades.
Na operação de divisão inteira transportamos o algarismo que queremos para a posição das unidades.
'''