""" Matrizes sao elementos bidimensionais que servem pra guardar os dados """

''' As matrizes em pyhton sao tem como sua criaçao como se fossem duas listas a primeira sendo a quantidade de linhas onde a primeira linha é dada como zero '''

linha = int(input('qnts linhas '))
coluna = int(input('qnts colunas '))

matriz = [None] * linha
for i in range(linha):
  matriz[i] = [None] * coluna
  for j in range(coluna):
    matriz[i][j] = int(input('Digite os elementos da matriz'))
print(matriz)