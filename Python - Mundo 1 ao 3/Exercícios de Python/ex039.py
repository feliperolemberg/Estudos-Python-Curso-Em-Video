from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, date.today().year))
if idade < 18:
    print('Ainda está cedo para você se alistar ao serviço militar obrigatório. Volte mais precisamente daqui a {} ano(s), em {}.'.format((18-idade), date.today().year + (18-idade)))
elif idade > 18:
    print('Você já passou do período de alistamento. Ultrapassou {} ano(s), mais precisamente foi em {}.'.format(idade-18, date.today().year - (idade-18)))
else:
    print('Está na hora de você se alistar! Procure a Junta de Serviço Militar mais próxima da sua região.')
