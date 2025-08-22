num = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
c = 0
print('Os primeiros 10 termos dessa PA são:')
while c != 10:
    print('{} → '.format(num) if c < 9 else '{}.'.format(num), end='')
    num = num + raz
    c += 1