lado1 = float(input('Digite o valor do primeiro segmento de reta: '))
lado2 = float(input('Digite o valor do segundo segmento de reta: '))
lado3 = float(input('Digite o valor do terceiro segmento de reta: '))
if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print('Esses três segmentos de reta juntos \033[32mpodem\033[m formar um triângulo.')
else:
    print('Esses três segmentos de reta juntos \033[31mNÃO podem\033[m formar um triângulo.')