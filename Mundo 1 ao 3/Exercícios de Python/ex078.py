# Quando você iguala listas, estabelece uma ligação entre elas
lista = []
listaposmaior = []
listaposmenor = []
for i in range(0, 5):
    valor = int(input(f'Digite um valor numérico inteiro para a posição {i}: '))
    lista.append(valor)
    if i == 0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
for c in range(len(lista)):
    if lista[c] == maior:
        listaposmaior.append(c)
    if lista[c] == menor:
        listaposmenor.append(c)
print('-=-'*16)
print(f'Você digitou os valores {lista}.')
print(f'O maior valor digitado foi o {maior} na(s) posição(ões) ', end='')
'''for p, ele in enumerate(lista):
    if ele == maior:
        print(f'{p}... ', end='')'''
for x in listaposmaior:
    print(f'{x}... ', end='')
print(f'\nO menor valor digitado foi o {menor} na(s) posição(ões) ', end='')
for y in listaposmenor:
    print(f'{y}... ', end='')