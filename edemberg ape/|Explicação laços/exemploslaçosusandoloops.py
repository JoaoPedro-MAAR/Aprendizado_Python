for a in range(10):
  print("IFPB")
for b in range(1, 51, 1):
  print(b)

numero = int(input('Digite quantas vezes voce deseja ser perguntado: '))
for c in range(numero):
  numero2 = int(input('Digite um numéro: '))
  print(f'Esse é seu dobro {numero2 * 2}')

soma = 0
numero3 = int(input('Digite quantas vezes voce deseja ser perguntado: '))
for c in range(numero3):
  numero4 = int(input('Digite um numéro: '))
  soma = numero4 + soma
print(soma)

#Esse efeito da soma so é possivel pois se da o valor 0 antes,ou seja no primeiro numero disposto no for a soma sera igual a ele,mas quando entra na nova istancia de FOR a soma sera, SOMA = NUMERONOVO + NUMEROANTERIOR, assim fazendo com que ocorra isso ate o final
