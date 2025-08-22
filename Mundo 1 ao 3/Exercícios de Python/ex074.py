from random import randint
tupla = ()
for c in range(0, 5):
    numgerado = randint(0, 10)
    tupla += (numgerado,)
    if c == 0:
        maior = numgerado
        menor = numgerado
    if numgerado > maior:
        maior = numgerado
    if numgerado < menor:
        menor = numgerado
print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')