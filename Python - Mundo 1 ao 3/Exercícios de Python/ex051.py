primeirotermo = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos dessa PA são: ')
for c in range(primeirotermo, primeirotermo + (10*raz), raz):
    print(c, end=' ')