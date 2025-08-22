peso = float(input('Digite o seu peso (em kg): '))
altura = float(input('Digite a sua altura (em metros): '))
imc = peso / (altura)**2
print('Seu IMC é {:.2f}.'.format(imc))
if imc > 40:
    print('Você têm \033[31mobesidade mórbida\033[m!')
elif imc > 30:
    print('Você têm \033[31mobesidade\033[m!')
elif imc > 25:
    print('Você têm \033[31msobrepeso\033[m!')
elif imc > 18.5:
    print('Você está no seu \033[32mpeso ideal\033[m!')
else:
    print('Você está \033[31mabaixo\033[m do peso!')
