from random import randint
from time import sleep
print('\033[30m-=-' *10 + '\033[m\n\033[33mEscolhendo um número de 0 a 5...\033[m\n' + '\033[30m-=-' * 10 + '\033[m')
num = randint(0,5)
chute = int(input('Tente acertá-lo: '))
print('\033[33mPROCESSANDO...\033[m')
sleep(2)
if chute == num:
    print('\033[32mParabéns!\033[m Você acertou o número escolhido por mim.')
else:
    print('\033[31mErrou!\033[m Eu pensei no {} e não no {}. Sua assertividade não está afiada.'.format(num, chute))
