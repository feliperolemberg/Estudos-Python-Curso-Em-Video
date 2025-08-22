somatorio = 0
contador = 0
for c in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        somatorio += num
        contador += 1
print('A soma dos {} números pares digitados é igual a {}.'.format(contador, somatorio))
