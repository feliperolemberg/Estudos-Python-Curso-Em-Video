num = int(input('Digite um número inteiro: '))
contador = 0
for c in range(1, num+1):
    if (num % c) == 0:
        contador += 1
if contador == 0 or contador == 1:
    print('O {} não é nem primo nem composto.'.format(num))
elif contador == 2:
    print('O {} é um número primo.'.format(num))
else:
    print('O {} é um número composto.'.format(num))