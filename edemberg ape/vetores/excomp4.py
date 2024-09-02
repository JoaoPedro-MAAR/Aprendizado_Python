''' 4. Escreva um programa para ler 6 números distintos, ou seja, não podem repetir.
Exiba os números lidos.'''
contagem = 1
vetor = []
while contagem <= 6:
  valor = int(input('Digite um valor: '))
  if vetor.count(valor) <= 0:
    vetor.append(valor)
    contagem += 1
  else:
    print('Valor invalido')

print(vetor)

#Na linha 7 poderia ser trocado por valor in vetor
