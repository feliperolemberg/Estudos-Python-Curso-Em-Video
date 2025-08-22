print('\033[33m-=-'*8 + '\n\033[30m EMPRÉSTIMO BANCÁRIO \033[m\n' + '\033[33m-=-'*8 + '\033[m')
valorcasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = float(input('Em quantos anos você pretende pagar? '))
valormensal = valorcasa / (anos*12)
if valormensal > (salario*0.3):
    print('O empréstimo foi \033[31mNEGADO\033[m! O valor calculado para a sua pretação mensal (\033[32mR${:.2f}\033[m) ultrapassou o limite permitido baseado no seu salário.'.format(valormensal))
else:
    print('O empréstimo foi \033[32mAPROVADO\033[m!\nO valor da sua prestação mensal ficou em: \033[32mR${:.2f}\033[m.'.format(valormensal))