num = int(input('Digite um número inteiro: '))
escolha = (str(input('Quer continuar (S/N)? '))).upper().strip()
maior = num
menor = num
c = 1
soma = num
while escolha == 'S':
    num = int(input('Digite outro número inteiro: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    c+=1
    escolha = (str(input('Quer continuar (S/N)? '))).upper().strip()
if c == 1:
    print('Você digitou apenas 1 número, o {}. Não há como calcular média ou fazer comparações de maior e menor com apenas isso. Tente \033[31mnovamente\033[m!'.format(num))
else:
    print("""O maior valor entre os digitados foi o {}.
O menor valor entre os digitados foi o {}.
A média aritmética dos {} números digitados é igual a {:.2f}.
""".format(maior, menor, c, soma/c))
