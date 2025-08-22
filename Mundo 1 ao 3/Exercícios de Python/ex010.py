valor = float(input('Quanto dinheiro você têm na carteira? R$'))
conversão = valor/5.8
print('Com R${} você pode comprar US${:.2f}.'.format(valor, conversão))
