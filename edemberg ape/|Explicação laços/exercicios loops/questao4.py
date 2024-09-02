
maior = 0
for k in range (1,21,1):
  numero = int(input('Digite um valor: '))
  if (maior < numero):
    maior = numero
  else:
    maior = maior
print(f'O maior numero é:{maior}')