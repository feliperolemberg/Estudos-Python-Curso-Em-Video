largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print('Sua parede têm dimensão {}x{} e sua área é {:.2f} metros quadrados.\nPara pintar essa parede, você precisará de {:.2f}l de tinta.'.format(largura, altura, area, (area/2)))
