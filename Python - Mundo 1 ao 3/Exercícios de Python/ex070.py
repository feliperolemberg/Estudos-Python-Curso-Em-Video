totalcompra = qtdmaiormil = c = 0
while True:
    print('-=-' * 7 + '\n Loja \033[1;32mSuper Baratão\033[m\n' + '-=-' * 7)
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço desse produto: R$'))
    if c == 0 or preco < menor:
        menor = preco
        nomemenor = produto
    while True:
        opcao = input('Deseja continuar (S/N)? ').upper().strip()
        if opcao in 'SN':
            break
    totalcompra += preco
    if preco > 1000:
        qtdmaiormil += 1
    c += 1
    if opcao == 'N':
        break
print(f"""{'\033[1;31m FIM\033[m do programa ':-^33}
Total gasto na compra R${totalcompra:.2f}.
{qtdmaiormil} produto(s) custa(m) mais que R$1000.00.
{nomemenor} é o produto mais barato custando R${menor:.2f}.""")
