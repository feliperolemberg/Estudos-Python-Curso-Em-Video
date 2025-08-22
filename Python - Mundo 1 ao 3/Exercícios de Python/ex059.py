from time import sleep
valor1 = int(input('Digite um primeiro valor inteiro: '))
valor2 = int(input('Digite outro valor inteiro: '))
escolha = 0
while escolha != 5:
    escolha = int(input("""--- O que você deseja fazer com esses dois valores? ---
[1] para somá-los
[2] para multiplicá-los
[3] para descobrir o maior entre os dois
[4] para digitar novos números
[5] para sair do programa
Digite a opção escolhida: """))
    if escolha == 1:
        print('A soma entre {} e {} é igual a {}.'.format(valor1, valor2, valor1+valor2))
    elif escolha == 2:
        print('O produto entre {} e {} é igual a {}.'.format(valor1, valor2, valor1*valor2))
    elif escolha == 3:
        if valor2 > valor1:
            print('O maior é o {}.'.format(valor2))
        elif valor1 == valor2:
            print('Os valores são iguais.')
        else:
            print('O maior é o {}.'.format(valor1))
    elif escolha == 4:
        valor1 = int(input('Digite um primeiro valor inteiro: '))
        valor2 = int(input('Digite outro valor inteiro: '))
    elif escolha == 5:
        print('Saindo...')
        sleep(1)
    else:
        print('Opção \033[31minválida\033[m!')