from emoji import emojize
from random import randint
from time import sleep
print('\033[33m-=-'*3 + '\n \033[m\033[7;97;40mJOKENPÔ\033[m\n\033[33m' + '-=-'*3 + '\033[m')
escolhamaquina = randint(1, 3)
escolhausuario = int(input(emojize('Vamos jogar \033[7;97;40mJOKENPÔ\033[m, digite a sua opção escolhida:\n\033[32m1\033[m - Pedra :mountain:\n\033[34m2\033[m - Papel :page_with_curl:\n\033[35m3\033[m - Tesoura :scissors:\n')))
tradumaquina = 'pedra'
traduusuario = 'pedra'
# Registrando a jogada em uma str
if escolhamaquina == 2:
    tradumaquina = 'papel'
elif escolhamaquina == 3:
    tradumaquina = 'tesoura'
if escolhausuario == 2:
    traduusuario = 'papel'
elif escolhausuario == 3:
    traduusuario = 'tesoura'
# Efeitos
print('\033[32mJO\033[m')
sleep(1)
print('\033[34mKEN\033[m')
sleep(1)
print('\033[35mPÔ!!!\033[m')
# Verificação do vencedor
if escolhamaquina == escolhausuario:
    print('Deu \033[97mEMPATE\033[m! Nós escolhemos {}.'.format(tradumaquina))
elif (escolhamaquina == 1 and escolhausuario == 3) or (escolhamaquina == 2 and escolhausuario == 1) or (escolhamaquina == 3 and escolhausuario == 2):
    print('Você \033[31mPERDEU\033[m! Eu escolhi {} e você escolheu {}.'.format(tradumaquina, traduusuario))
elif (escolhamaquina == 1 and escolhausuario == 2) or (escolhamaquina == 2 and escolhausuario == 3) or (escolhamaquina == 3 and escolhausuario == 1):
    print('Você \033[32mGANHOU\033[m! Eu escolhi {} e você escolheu {}.'.format(tradumaquina, traduusuario))
else:
    print('Escolha \033[31mINVÁLIDA\033[m! Tente novamente.')
