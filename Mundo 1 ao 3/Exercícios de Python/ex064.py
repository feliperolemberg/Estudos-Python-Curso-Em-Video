print('~=~'*10)
entrada = int(input("""Para \033[31mSAIR\033[m digite [999]
Digite um número inteiro: """))
soma = 0
c = 0
while entrada != 999:
    soma += entrada
    c+=1
    print('~=~'*10)
    entrada = int(input("""Para \033[31mSAIR\033[m digite [999]
Digite outro número inteiro: """))
if c == 0:
    print('~=~'*16)
    print('Você não digitou nenhum número! Tente novamente.')
    print('~=~' * 16)
elif c == 1:
    print('~=~'*12)
    print('Você digitou apenas um número, o {}.'.format(soma))
    print('~=~' * 12)
else:
    print('~=~'*20)
    print('A soma de todos os {} números que você digitou é igual a {}.'.format(c, soma))
    print('~=~'*20)