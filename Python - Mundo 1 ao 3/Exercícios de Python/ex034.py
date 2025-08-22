salario = float(input('Digite o valor do seu salário: R$'))
if salario > 1250:
    nsalario = salario * 1.10
    print('O seu salário com aumento ficou em {:.2f}.'.format(nsalario))
else:
    nsalario = salario * 1.15
    print('O seu salário com aumento ficou em {:.2f}.'.format(nsalario))
