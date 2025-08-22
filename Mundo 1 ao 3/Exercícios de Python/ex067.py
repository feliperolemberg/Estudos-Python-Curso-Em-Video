while True:
    num = int(input('Digite um número inteiro (não negativo) e veja sua tabuada: '))
    if num < 0:
        break
    print('-~-' * 5)
    for c in range(1, 11):
        print(f'{num} * {c} = {num*c}')
    print('-~-' * 5)
print('Finalizando a execução do programa...')