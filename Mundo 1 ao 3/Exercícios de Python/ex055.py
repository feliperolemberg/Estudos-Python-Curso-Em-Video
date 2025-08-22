print('Digite o peso de 5 pessoas a seguir')
ppeso = float(input('Peso (em Kg): '))
menor = ppeso
maior = ppeso
for c in range(0, 4):
    peso = float(input('Peso (em Kg): '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso entre as 5 pessoas é {}Kg, e o menor é {}Kg.'.format(maior, menor))