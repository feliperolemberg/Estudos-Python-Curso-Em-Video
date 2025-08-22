num = int(input('Digite um número inteiro positivo para calcular o seu fatorial: '))
cont = num
somatorio = 1
print('{}! = '.format(num), end='')
while cont != 0:
    somatorio = somatorio * cont
    print('{} x '.format(cont) if cont > 1 else '{} '.format(cont), end='')
    cont -= 1
print('= {}.'.format(somatorio))

'''
num = int(input('Digite um número inteiro positivo: '))
somatorio = 1
for c in range(num, 0, -1):
    somatorio = somatorio * c
print('O fatorial de {} é igual a {}.'.format(num, somatorio))
'''