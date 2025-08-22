print('Sabe qual é a soma de todos os números ímpares que são múltiplos de três entre 1 e 500?')
somatorio = 0
contador = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        somatorio = somatorio + c
        contador += 1
print('A soma dos {} número existentes geram o resultado é igual a {}.'.format(contador, somatorio))