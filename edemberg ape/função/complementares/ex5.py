import random


def gerMATRIZ(lin,col):

  matriz1 = [None] * lin
  for i in range(lin):
    matriz1[i] = [None] * col
    for j in range(col):
      matriz1[i][j] = random.randint(0,4)

  return matriz1

def visual(matriz):
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      print(f'{matriz[i][j]:4}',end='')
      print()
  
      
def soma_matriz(matriz_1 , matriz_2):
  matriz_soma = [None] * len(matriz_1)
  for i in range(len(matriz_1)):
    matriz_soma[i] = [None] * len(matriz_1[0])
    for j in range(len(matriz_2[i])):
      matriz_soma[i][j] = matriz_1[i][j] + matriz_2[i][j]


lin = int(input('QUantos linhas '))
col = int(input('Quantas colunas'))
matriz_1 = gerMATRIZ(lin,col)
matriz_2 = gerMATRIZ(lin,col)
visual(matriz_1)
visual(matriz_2)
soma_matriz(matriz_1,matriz_2)

    
  
    
  