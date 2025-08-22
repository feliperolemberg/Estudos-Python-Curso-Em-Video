num = int(input('Digite um número: '))
print('O \033[35mdobro\033[m desse número é igual a \033[36m{}\033[m\nO \033[35mtriplo\033[m desse número é igual a \033[36m{}\033[m\nA \033[35mraiz quadrada\033[m desse número é igual a \033[36m{:.2f}\033[m.'.format((num*2), (num*3), (pow(num, 0.5))))
