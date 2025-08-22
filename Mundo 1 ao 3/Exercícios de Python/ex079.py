opcao = 'S'
lista = []
while opcao == 'S':
    c = 0
    numero = int(input('Digite um valor para ser adicionado: '))
    for i in lista:
        if numero == i:
            c+=1
    if c > 0:
        print('Valor \033[31mduplicado\033[m! Não vou adicionar.')
        opcao = input('Deseja continuar?[S/N] ').strip().upper()
        continue
    lista.append(numero)
    print('Valor adicionado com \033[32msucesso\033[m...')
    opcao = input('Deseja continuar?[S/N] ').strip().upper()
lista.sort()
print('-=-'*22)
print(f'O(s) número(s) adicionado(s) em ordem crescente é/são {lista}.')
