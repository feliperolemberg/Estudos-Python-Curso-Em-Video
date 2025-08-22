nume = int(input('Digite um número para ver sua tabuada até o 10: '))
print('\033[30m-=-\033[m'*5)
for c in range(1, 11):
    print('{} x \033[33m{}\033[m = \033[32m{}\033[m'.format(nume, c, nume*c))
print('\033[30m-=-\033[m'*5)
