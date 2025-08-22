numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
digitado = int(input('Digite um número entre 0 e 20: '))
while digitado > 20 or digitado < 0:
   digitado = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'O número digitado foi o {numeros[digitado]}!')
"""
while True:
    while True:
        digitado = int(input('Digite um número entre 0 e 20: '))
        if 0 <= digitado <= 20:
            break
        print('Tente novamente! ', end='')
    print(f'O número digitado foi o {numeros[digitado]}!')
    opcao = input('Você deseja continuar (S/N)? ').upper().strip()
    if opcao == 'N':
        break
"""