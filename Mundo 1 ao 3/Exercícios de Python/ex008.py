distancia = float(input('Uma distância em metros: '))
print('A distância {}m corresponde a:'.format(distancia))
print('{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format((distancia/1000), (distancia/100), (distancia/10), (distancia*10), (distancia*100), (distancia*1000)))
