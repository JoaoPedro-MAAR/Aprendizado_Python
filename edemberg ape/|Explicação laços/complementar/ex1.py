"""Faça um programa que leia um número N, calcule e mostre os N primeiros
termos da sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13, ...). O valor lido para
N sempre será maior ou igual a 2."""
ultimo = 1
antes = 0
N = int(input('Digite quantos termos você quer da sequencia Fibonacci: '))
for k in range(antes , N-2, ultimo):
  prox = antes + ultimo 
  aux = antes
  antes = ultimo
  ultimo = aux
  ultimo = prox


  print(prox)
print(prox,antes,ultimo)