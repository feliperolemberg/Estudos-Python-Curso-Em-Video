nome = str(input('Digite o seu nome completo: '))
nome_div = nome.split()
primeiro_nome = nome_div[0]
nome_div_inv = nome_div[::-1]
print(nome_div_inv)
ultimo_nome = nome_div_inv[0]
print('O seu primeiro nome é \033[32m{}\033[m.'.format(primeiro_nome))
print('O seu último nome é \033[32m{}\033[m.'.format(ultimo_nome))
