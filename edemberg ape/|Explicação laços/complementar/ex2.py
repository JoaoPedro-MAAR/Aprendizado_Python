"""2. Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele
próprio. Faça um programa que mostre todos os números primos de 1 a N
(obs: N será lido)."""

n = int(input('Quantos termos primos vocẽ quer '))
for k in range(2,n+1):
  primo = True
  for i in range(2,k):
    if k%i == 0:
      primo = False
      continue
  if primo:
    print(k)
      