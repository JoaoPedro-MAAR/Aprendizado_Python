def somar(bla):
  soma = 0
  for i in range(TAMANHO):
    soma += bla[i] 
  return soma
TAMANHO = int(input('Qual o tamanho do vetor: '))
bla = [None] * TAMANHO
for i in range(TAMANHO):
  bla[i] = int(input('Diga me o numero: '))
print(somar(bla))
print()