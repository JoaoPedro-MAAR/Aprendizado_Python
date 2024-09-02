vetor = [None]*6
count = -1
vetor_par = [None]*3
vetor_impar = [None]*3
cont_par = 0
cont_impar = 0
for i in range(6):
  count = count + 1
  if count%2 == 0:
    vetor[i] = int(input('digite valor: '))
    for b in range(cont_par , 3):
      cont_par += 1   
      vetor_par[b] = vetor[i]
      break
  else:
    vetor[i] = int(input('digite valor: '))
    for b in range(cont_impar, 3):
      cont_impar += 1
      vetor_impar[b] = vetor[i]
      break

print(f'esse é o vetor principal:{vetor}')
print(f'esse sao os elementos que aparecem nos indices pares:{vetor_par}')
print(f'esse sao os elementos que aparecem nos indices impares:{vetor_impar}')
