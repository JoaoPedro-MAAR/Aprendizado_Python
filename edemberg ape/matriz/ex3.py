import random

LINHA = 3
print(LINHA)
matriz = [None] * LINHA
teste = LINHA - 1
matrizb = [None] * LINHA



for ai in range(LINHA):
  matriz[ai] = [None] * LINHA
  for aj in range(LINHA):
    matriz[ai][aj] = int(input('Digite numero'))
for ai in range(LINHA):
  for aj in range(LINHA):
    print(f'{matriz[ai][aj]:4}',end='')
  print()
print(matriz[1][2])

for ai in range(LINHA):
  matrizb[ai] = [0] * LINHA
  for aj in range(LINHA):
    if ai == aj or ai + aj == teste:
      matrizb[ai][aj] = 0
      continue
    elif ai != aj:
      a = ai + aj
      matrizb[ai][aj] = a + matriz[ai][aj]
      continue


for ai in range(LINHA):
  for aj in range(LINHA):
    print(f'{matrizb[ai][aj]:4}',end='')
  print()





    
    
    
  
  