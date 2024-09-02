''' funçoes range sao utilizados para controlar o for , com três parâmetros o start, o stop , e step,servindo respectivamente para,o start diz onde começa, o stop diz onde termina,mas atente-se pois o stop tem um intervalo aberto ou seja,sera necessario botar o stop sempre com +1, e o step diz quanto sera o intervalo
Exemplo:
'''
for x in range(1,5):
  print(x)
### Nota-se que o step nao sera necessario quando o intervalo entr elementos for 1  

for y in range(1,11,2):
  print(f'{x} e {y} ')

for z in range(50,301,5):
  print(z)
### Nota que pode ser feito usando o O STOP,mas usando desse jeito o START sera definido como 0 e o STEP como 1
for X in range(4):
  print("IFPB")


"""Note também que podera ser feito ao contrario usando um intervalo negativo siga o exemplo"""

for Z in range(20,-1,-10):
  print('Bla')