preco = float(input('Qual o preço do produto? \033[32mR$\033[m'))
condicao = int(input('Qual a condição de pagamento? Digite a seguir:\n\033[33m[ 1 ]\033[m - À VISTA (dinheiro ou pix)\n\033[33m[ 2 ]\033[m - À VISTA NO CARTÃO\n\033[33m[ 3 ]\033[m - EM ATÉ 2X NO CARTÃO\n\033[33m[ 4 ]\033[m - 3X OU MAIS NO CARTÃO\n'))
if condicao == 1:
    print('Para pagamento à vista (dinheiro ou pix), o preço do produto com desconto fica em R${:.2f}.'.format(preco*0.9))
elif condicao == 2:
    print('Para pagamento à vista no cartão, o preço do produto com desconto fica em R${:.2f}.'.format(preco*0.95))
elif condicao == 3:
    print('Para pagamento em 2x no cartão, ficarão 2 parcelas de R${:.2f}\n O total a pagar permanece em R${:.2f}.'.format(preco/2, preco))
elif condicao == 4:
    parcelas = int(input('Quantas vezes no cartão? '))
    print('Para pagamento em {}x no cartão, ficarão {} parcelas de R${:.2f}. Pois entra juros.\nTotal a pagar fica em R${:.2f}.'.format(parcelas, parcelas, (preco*1.2) / parcelas, preco * 1.2))
else:
    print('Opção inválida! Tente novamente.')