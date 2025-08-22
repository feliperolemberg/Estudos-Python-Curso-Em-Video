frase = (input('Digite uma frase: ')).strip().lower()
frasese = frase.replace(' ', '')
fraseseinv = frasese[::-1]
qcaracteres = len(frasese)
if qcaracteres == len(fraseseinv):
    contador = 0
    for c in range(0, qcaracteres):
        if frasese[c] == fraseseinv[c]:
            contador += 1
    if contador == qcaracteres:
        print('Esta frase \033[32mÉ\033[m um palíndromo!')
    else:
        print('Esta frase \033[31mNÃO\033[m é um palíndromo!')
else:
    print('Esta frase \033[31mNÃO\033[m é um palíndromo!')
