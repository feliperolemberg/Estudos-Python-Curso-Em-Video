lista = []
opcao = 'S'
c = 0
while opcao == 'S':
    num = int(input('Digite um valor inteiro: '))
    lista.append(num)
    c+=1
    opcao = input('Deseja continuar?[S/N] ').upper().strip()
listaoriginal = lista[:]
lista.sort(reverse=True)
print(f"""Aqui está a lista: {listaoriginal}.
Foram digitados {c} números.
Aqui está a lista ordenada de forma descrescente: {lista}.""")
print('O valor 5 está na lista!' if 5 in lista else 'O valor 5 não está na lista!')
