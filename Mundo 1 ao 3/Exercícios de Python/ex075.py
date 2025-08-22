tupla = ()
tuplapares = ()
pos = -1
for c in range(4):
    valor = int(input('Digite um valor inteiro: ' if c == 0 else 'Digite outro valor inteiro: '))
    tupla += (valor,)
    if valor == 3 and pos == -1:
        pos = c+1
    if valor % 2 == 0:
        tuplapares += (valor,)
print(f"""Você digitou os valores {tupla}.
O valor 9 apareceu {tupla.count(9)} vez(es).""")
print('O valor 3 não foi digitado em nenhuma posição' if pos == -1 else f'O valor 3 apareceu na {pos}ª posição.')
print(f'Os valor par digitado foi o {tuplapares[0]}' if len(tuplapares) == 1 else f'Os valores pares digitados foram {tuplapares}.')

