cidade = str(input('Digite o nome da cidade: '))
pncidade = cidade.split()[0]
print('O nome da cidade começa com "Santo"?', 'santo' in pncidade.lower())
