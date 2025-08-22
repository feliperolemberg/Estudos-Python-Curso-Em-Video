nome = str(input('Qual é o seu nome? '))
if nome == 'Felipe':
    print('Que nome \033[32mbonito\033[m!')
elif nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Florelina Regina':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia \033[35m{}\033[m!'.format(nome))
