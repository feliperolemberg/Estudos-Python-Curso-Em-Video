lista = list()
for c in range(5):
    valor = int(input('Digite um valor inteiro para ser adicionado na lista: '))
    if c == 0:
        lista.append(valor)
        print(f'Primeiro número, portanto, adicionado na posição de número {c} da lista.')
    else:
        for i in range(len(lista)):
            if valor <= lista[i]:
                lista.insert(i, valor)
                print(f'Número adicionado na posição de número {i} da lista.')
                break
            elif i == (len(lista)-1) and valor >= lista[i]:
                lista.append(valor)
                print(f'Número adicionado no final! Na posição de número {i+1} da lista.')
print('-=-'*20)
print(f'Os valores digitados em ordem são {lista}.')
