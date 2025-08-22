num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 == num2:
    print('Não existe valor maior, os dois números são iguais.')
elif num2 > num1:
    print('O segundo valor é maior.'.format(num2))
else:
    print('O primeiro valor é maior.'.format(num1))
