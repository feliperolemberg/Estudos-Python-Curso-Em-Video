dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro rodou? '))
valor = (dias*60) + (0.15*km)
print('O total a pagar é R${:.2f}'.format(valor))
