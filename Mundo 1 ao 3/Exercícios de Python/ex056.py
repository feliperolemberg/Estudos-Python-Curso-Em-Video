print('Digite o nome, a idade e o sexo de 4 pessoas.')
somatorioid = 0
contadorf = 0
mvhomem = 0
nmvhomem = ''
for c in range(0, 4):
    print('-=-' * 8)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M ou F): '))
    somatorioid += idade
    if c == 0 and sexo == 'M':
        mvhomem = idade
        nmvhomem = nome
    if idade > mvhomem and sexo == 'M':
        mvhomem = idade
        nmvhomem = nome
    if sexo == 'F' and idade < 20:
        contadorf += 1
print('A média de idade do grupo é {} anos.'.format(somatorioid/4))
if nmvhomem == '':
    print('Não foi digitado nenhum homem, portanto, não existe homem mais velho.')
else:
    print('{} é o nome do homem mais velho, ele possui {} anos.'.format(nmvhomem, mvhomem))
print('{} mulher(es) têm menos de 20 anos.'.format(contadorf))