frase = str(input('Digite uma frase: ')).lower().strip()
quantidade_a = frase.count('a')
primeira_posicao_a = frase.find('a') + 1
ultima_posicao_a = frase.rfind('a') + 1
print('A letra \033[31m"a"\033[m apareceu \033[1m{}\033[m vezes na frase.'.format(quantidade_a))
print('A primeira letra \033[31m"a"\033[m aparece na posição \033[1m{}\033[m.'.format(primeira_posicao_a))
print('A ultima letra \033[31m"a"\033[m aparece na posição \033[1m{}\033[m.'.format(ultima_posicao_a))
