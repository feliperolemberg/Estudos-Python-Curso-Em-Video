lista = []
pares = []
impares = []
opcao = 'S'
while opcao == 'S':
    numero = int(input('Digite um número inteiro: '))
    lista.append(numero)
    opcao = input('Deseja continuar?[S/N] ').strip().upper()
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print('-=-' * 20)
print(f'A lista com todos os números digitados é {lista}.')
print(f'Não foram digitados números pares.' if len(pares) == 0 else f'A lista com todos os números pares digitados é {pares}.')
print(f'Não foram digitados números ímpares.' if len(impares) == 0 else f'A lista com todos os números ímpares digitados é {impares}')
