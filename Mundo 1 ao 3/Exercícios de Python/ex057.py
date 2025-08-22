sexo = (str(input('Digite o seu sexo (F/M): '))).upper().strip()
while sexo != 'F' and sexo != 'M':
    print('Resposta \033[31minválida\033[m.')
    sexo = (str(input('Digite novamente o seu sexo (F/M): '))).upper()
print('Ok, o seu sexo foi cadastrado como', 'masculino.' if sexo == 'M' else 'feminino.')
