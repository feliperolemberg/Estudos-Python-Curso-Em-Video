num = int(input('Digite um número inteiro: '))
conv = int(input('Digite a base de conversão desejada:\n\033[34m1\033[m para binário\n\033[34m2\033[m para octal\n\033[34m3\033[m para hexadecimal\n'))
if conv == 1:
    print('O número inteiro {} convertido para binário é {}.'.format(num, bin(num)[2:]))
elif conv == 2:
    print('O número inteiro {} convertido para octal é {}.'.format(num, oct(num)[2:]))
elif conv == 3:
    print('O número inteiro {} convertido para hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')