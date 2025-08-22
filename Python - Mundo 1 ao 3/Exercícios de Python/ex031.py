distancia = float(input('Qual a distância da viagem (em Km)? '))
if distancia <= 200:
    print('O preço da passagem é R${:.2f}.'.format(distancia*0.5))
else:
    print('O preço da passagem é R${:.2f}.'.format(distancia*0.45))
