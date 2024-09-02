'''2. Escreva um programa que:
• Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N contendo elementos
inteiros (N será lido);
• Exiba a matriz lida (no formato de matriz);
• Exiba os elementos da diagonal principal, isto é, os elementos onde I = J.'''




LINHA = int(input('Qual o tamanho da matriz quadrada: '))
lista =[]
matriz  = [None] * LINHA
for i in range(LINHA):
  matriz[i] = [None] * LINHA  
  for j in range(LINHA):
    matriz[i][j] = int(input('Digite numeros para matriz: '))
    if i == j:
      lista.append(matriz[i][j])
for i in range(LINHA):
  for j in range(LINHA):
    print(f'{matriz[i][j]:4}',end='')
  print()
print(lista)


