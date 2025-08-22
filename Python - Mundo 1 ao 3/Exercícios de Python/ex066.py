c = soma = 0
while True:
    n = int(input('Digite um número inteiro (999 caso queira parar): '))
    if n == 999:
        break
    soma += n
    c += 1
print(f'Foram digitados {c} números e a soma entre todos eles é igual a {soma}.')
