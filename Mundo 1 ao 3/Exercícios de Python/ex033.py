num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
menor = num1
maior = num1
# Verificação do menor
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
# Verificação do maior
if num2 > num1:
    maior = num2
if num3 > num1:
    maior = num3
if num1 == num2 and num1 == num3:
    print('Os três números são iguais. Portanto, o menor e maior número ao mesmo tempo é o próprio {}.'.format(num1))
else:
    print('O menor número é o {}.\nO maior número é o {}.'.format(menor, maior))