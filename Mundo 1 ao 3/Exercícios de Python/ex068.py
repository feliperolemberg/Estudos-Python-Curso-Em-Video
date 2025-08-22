from random import randint
print('\033[33m-=-\033[m' *  5 + '\n \033[1;97mPAR\033[m OU \033[1;97mÍMPAR\033[m\n' + '\033[33m-=-\033[m' * 5)
c = 0
while True:
    num = int(input('Escolha um número natural (Menor ou igual a 10): '))
    numgerado = randint(1, 10)
    s = num + numgerado
    escolha = ' '
    while escolha not in 'PI':
        escolha = input('Par ou ímpar (P/I)? ').strip().upper()[0]
    if (escolha == 'P' and (s % 2 == 0)) or (escolha == 'I' and (s % 2 != 0)):
        print('-=-' * 32 + f'\nVocê \033[32mganhou\033[m! Você jogou {num} e o computador {numgerado}. O total deu {s}', 'que é um número \033[32mpar\033[m, jogue novamente.' if (s % 2 == 0) else 'que é um número \033[32mímpar\033[m, jogue novamente.')
        c += 1
    else:
        print('-=-' * 28 + f'\nVocê \033[31mperdeu\033[m! Você jogou {num} e o computador {numgerado}. O total deu {s},', 'que é um número \033[31mpar\033[m.' if (s % 2 == 0) else 'que é um número \033[31mímpar\033[m.')
        break
print(f'No total você ganhou {c} vez(es).')