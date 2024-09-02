def fatorial(n):
  fator = n
  for i in range(1,n):
    fator = fator * i
  
  print(f'O fatorial de {n} é {fator}')
fatorial(int(input('Digite o numero para ser fatorado: ')))