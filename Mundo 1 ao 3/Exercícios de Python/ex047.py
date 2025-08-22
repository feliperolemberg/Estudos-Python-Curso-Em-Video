print('Sabe quantos números pares existem entre 1 e 50? São eles:')
qnum = 0
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end='; ')
        qnum += 1
print('\nTotalizando {} números pares entre 1 e 50.'.format(qnum))