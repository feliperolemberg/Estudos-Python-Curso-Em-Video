from datetime import date
anonasc = int(input('Digite o ano de nascimento do atleta: '))
idade = (date.today().year) - anonasc
print('O atleta possui {} anos.'.format(idade))
if idade > 25:
    print('Ele se encaixa na categoria \033[32mMASTER\033[m!')
elif idade > 19:
    print('Ele se encaixa na categoria \033[32mSÊNIOR\033[m!')
elif idade > 14:
    print('Ele se encaixa na categoria \033[32mJUNIOR\033[m!')
elif idade > 9:
    print('Ele se encaixa na categoria \033[32mINFANTIL\033[m!')
else:
    print('Ele se encaixa na categoria \033[32mMIRIM\033[m!')
