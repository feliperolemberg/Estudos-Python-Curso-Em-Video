n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número inteiro: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} número pares e {} números ímpares.'.format(par, impar))
