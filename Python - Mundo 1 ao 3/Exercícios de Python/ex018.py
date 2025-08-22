from math import sin, cos, tan, radians
ang = float(input('Digite o valor do ângulo em graus: '))
angrad = radians(ang)
print('O seno desse ângulo é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(sin(angrad), cos(angrad), tan(angrad)))
