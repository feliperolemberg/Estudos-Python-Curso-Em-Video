'''
nome = str(input('Qual é seu nome? '))
if nome == 'Felipe':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia {}.'.format(nome))
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.2f}.'.format(m))
print('Parabéns!' if m >= 7.0 else 'Estude mais!')
