from math import sqrt
catetooposto = float(input('Comprimento do cateto oposto: '))
catetoadja = float(input('Comprimento do cateto adjacente: '))
hip = sqrt((catetooposto**2) + (catetoadja**2))
# hip = hypot(catetooposto, catetoadja)
print('O comprimento da hipotenusa é {:.2f}.'.format(hip))
