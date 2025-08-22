expressao = input('Digite uma expressão que utilize parênteses: ').strip()
listaabertura = []
listafechamento = []
for c in range(len(expressao)):
    if expressao[c] == ')' and (len(listaabertura) == len(listafechamento)):
        listafechamento.append('FI') # Fechado incorretamente
    elif expressao[c] == '(':
        listaabertura.append('AC') # "Aberto corretamente"
    elif expressao[c] == ')' and (len(listaabertura) != len(listafechamento)):
        listafechamento.append('FC') # "Fechado corretamente"
if 'FI' in listafechamento or len(listaabertura) != len(listafechamento):
    print('Essa expressão está \033[31merrada\033[m!')
else:
    print('Sua expressão está \033[32mválida\033[m!')