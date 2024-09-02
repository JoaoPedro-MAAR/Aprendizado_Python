"""1. Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com
valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente). O programa
deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C).
Ao final, exiba as 3 matrizes (no formato de matriz)."""

LINHA = 2
COLUNA = 3

matriz_A = [None] * LINHA
for a1 in range(LINHA):
  matriz_A[a1] = [None] * COLUNA
  for a2 in range(COLUNA):
    matriz_A[a1][a2] = int(input('Digite os elementos A: '))
for a1 in range(LINHA):
  for a2 in range(COLUNA):
    print(f'{matriz_A[a1][a2]:4}',end='')
  print()

print(matriz_A)

matriz_B = [None] * LINHA
for b1 in range(LINHA):
  matriz_B[b1] = [None] * COLUNA
  for b2 in range(COLUNA):
    matriz_B[b1][b2] = int(input('Digite os elementos B: '))
for b1 in range(LINHA):
  for b2 in range(COLUNA):
    print(f'{matriz_B[b1][b2]:4}',end='')
  print()


print(matriz_B)

matriz_C = [None] * LINHA
for c1 in range(LINHA):
  matriz_C[c1] = [None] * COLUNA
  for c2 in range(COLUNA):  
    matriz_C[c1][c2] = matriz_A[a1][a2] +  matriz_B[b1][b2]
print(matriz_C)
    

print('Matriz A')
for a1 in range(LINHA):
  for a2 in range(COLUNA):
    print(f'{matriz_A[a1][a2]:4}',end='')
  print()

print('Matriz B')
for b1 in range(LINHA):
  for b2 in range(COLUNA):
    print(f'{matriz_B[b1][b2]:4}',end='')
  print()

print('Matriz C')
for c1 in range(LINHA):
  for c2 in range(COLUNA):
    print(f'{matriz_C[c1][c2]:4}',end='')
  print()














