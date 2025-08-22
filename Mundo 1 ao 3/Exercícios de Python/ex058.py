from random import randint
print('\033[30m-=-'*11 + '\033[m\n\033[33mEscolhendo um número de \033[97m0\033[m \033[33ma\033[m \033[97m10\033[33m...\033[m\n' + '\033[30m-=-'*11 + '\033[m')
num = randint(0, 10)
chute = int(input('Tente adivinhar o número escolhido: '))
c = 1
while chute != num:
    if chute > num:
        chute = int(input('\033[31mErrado\033[m! É menos. Tente novamente: '))
    else:
        chute = int(input('\033[31mErrado\033[m! É mais. Tente novamente: '))
    c += 1
if c == 1:
    print('\033[32mIncrível\033[m! Conseguiu acertar de primeira, sua assertividade está muito alta.')
else:
    print('\033[32mAcertou\033[m! Conseguiu acertar após {} tentativas.'.format(c))
