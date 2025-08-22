from time import sleep
print('-=-'*14)
num = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
print('-=-'*14)
escolha = 10
print('Os 10 primeiros termos dessa PA são: ')
c = 0
while escolha != 0:
    while escolha != 0:
        print('{} - '.format(num) if escolha > 1 else '{}.'.format(num), end='')
        num = num + raz
        escolha -= 1
        c += 1
    print('\n' + '-=-'*14)
    print('Você deseja mostrar mais termos da PA?\nSe \033[32mSIM\033[m, digite a quantidade de termos.\nSe \033[31mNÃO\033[m, digite 0.')
    escolha = int(input(''))
print('-=-'*15)
print('Progressão finalizada com {} termos mostrados.\nEncerrando...'.format(c))
sleep(1)