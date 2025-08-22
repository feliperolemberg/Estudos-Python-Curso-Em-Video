cmaior = chomens = cmulher20 = 0
while True:
    print('-+-' * 7 + '\n Cadastro de pessoas\n' + '-+-' * 7)
    idade = int(input('Digite a sua idade: '))
    while True:
        sexo = input('Digite o seu sexo (M/F): ').upper().strip()
        if sexo in 'MF':
            break
    while True:
        opcao = input('Deseja continuar cadastrando (S/N)? ').upper().strip()[0]
        if opcao in 'SN':
            break
    if idade >= 18:
        cmaior += 1
    if sexo == 'M':
        chomens += 1
    if idade < 20 and sexo == 'F':
        cmulher20 += 1
    if opcao == 'N':
        break
print('-=-' * 16 + f"""\nFim do programa
{cmaior} pessoa(s) é/são maior(es) de idade.
{chomens} é/são homem(ns).
{cmulher20} é/são mulher(es) e possui(em) menos de 20 anos.\n""" + '-=-' * 16)