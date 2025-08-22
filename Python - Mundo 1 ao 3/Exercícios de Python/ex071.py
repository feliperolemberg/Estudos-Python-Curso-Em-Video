print('=-=' * 4 + '\n \033[1;97mBANCO CEV\033[m\n' + '=-=' * 4)
valor = int(input('Digite o valor a ser sacado: R$'))
print('Serão obtidas: ')
ced50 = valor // 50
resto50 = valor - (50*ced50)
ced20 = resto50 // 20
resto20 = resto50 - (20*ced20)
ced10 = resto20 // 10
resto10 = resto20 - (10*ced10)
ced1 = resto10 / 1
if ced50 > 0:
    print(f'{int(ced50)} cédula(s) de R$50,00.')
if ced20 > 0:
    print(f'{int(ced20)} cédula(s) de R$20,00.')
if ced10 > 0:
    print(f'{int(ced10)} cédula(s) de R$10,00.')
if ced1 > 0:
    print(f'{int(ced1)} cédula(s) de R$1,00.')
'''total = valor
cedulaatual = 50
totalcedulas = 0
while True:
    if total >= cedulaatual:
        total -= cedulaatual
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'{totalcedulas} cédulas de R${cedulaatual},00.')
        if cedulaatual == 50:
            cedulaatual = 20
        elif cedulaatual == 20:
            cedulaatual = 10
        elif cedulaatual == 10:
            cedulaatual = 1
        else:
            break
        totalcedulas = 0'''
print('=-=' * 15 + '\nVolte sempre ao \033[1;97mBANCO CEV\033[m! Tenha um bom dia!')