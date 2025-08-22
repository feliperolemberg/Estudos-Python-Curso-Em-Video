palavras = ('Flamengo', 'Madrid', 'Arrascaeta', 'Gabigol', 'Ronaldo', 'Python', 'Felipe', 'Milly', 'Champions', 'Brasil', 'Trabalho', 'Mental', 'Velocidade', 'Amor', 'Foco')
for c in range(len(palavras)):
    tupla = ()
    for l in range(len(palavras[c])):
        if palavras[c][l] in 'aeiou' or palavras[c][l] in 'AEIOU':
            tupla += (palavras[c][l],)
    print(f'Na palavra {palavras[c]} temos ', end='')
    for i in range(len(tupla)):
        if i == (len(tupla) - 1):
            print(f'{tupla[i]}.')
        else:
            print(f'{tupla[i]}', end =' ')
#print(f'Na palavra {palavras[c]} temos {tupla} como vogais.' if len(tupla) > 1 else f'Na palavra {palavras[c]} temos apenas a vogal {tupla[0]}.')
