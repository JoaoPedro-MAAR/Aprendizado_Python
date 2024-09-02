vetor = [None]*10



cont = 0
k = int(input('Qual o valor voce quer procurar '))
for i in range(10):
  vetor[i] = int(input(f'Digite o {i+1} valor:  '))
  if vetor[i] == k:
    cont += 1
print(f'O valor {k} apareceu {cont} vezes')
  