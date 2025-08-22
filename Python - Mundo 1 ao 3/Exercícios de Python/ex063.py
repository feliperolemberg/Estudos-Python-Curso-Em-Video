n = int(input('Quantos termos da Sequência de Fibonacci você deseja ver? '))
antepenultimo = 0
penultimo = 1
print('Os {} primeiros termos da Sequência de Fibonacci são:'.format(n))
print(antepenultimo, penultimo, end=' ')
while (n-2) != 0:
    termoatual = antepenultimo + penultimo
    print(termoatual, end=' ')
    antepenultimo = penultimo
    penultimo = termoatual
    n -= 1  