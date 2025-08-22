nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
m = (nota1+nota2)/2
print('Tirando {} e {}, a média do aluno é {:.1f}.'.format(nota1, nota2, m))
if m >= 7:
    print('\033[32mAPROVADO!\033[m')
elif m < 5:
    print('\033[31mREPROVADO!\033[m')
else:
    print('\033[36mRECUPERAÇÃO!\033[m')
