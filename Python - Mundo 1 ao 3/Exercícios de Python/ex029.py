velocidade = float(input('Qual a velocidade do carro (em Km/h)? '))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print('Você \033[31multrapassou\033[m o limite permitido de 80Km/h e será \033[31mmultado\033[m! A multa custará R${:.2f}.'.format(multa))
else:
    print('Você \033[32mnão ultrapassou\033[m o limite permitido de 80Km/h. Continue assim!')
print('Tenha um bom dia, dirija com segurança.')
