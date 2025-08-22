lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))
if (lado1+lado2) > lado3 and (lado1+lado3) > lado2 and (lado2+lado3) > lado1:
    print('Eles \033[32mpodem\033[m formar um triângulo.')
    if lado1 == lado2 == lado3:
        print('E formariam um triângulo equilátero.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('E formariam um triângulo isósceles.')
    else:
        print('E formariam um triângulo escaleno.')
else:
    print('Eles \033[31mnão podem\033[m formar um triângulo.')