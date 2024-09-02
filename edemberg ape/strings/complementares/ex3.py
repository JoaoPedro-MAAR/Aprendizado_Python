nome = input('Digite seu nome completo: ').upper()
nome_split = nome.split()
print(f'{nome_split[len(nome_split) - 1]} ', end='')
for i in range(len(nome_split) - 1):
  print(f'{nome_split[i][0] }.' , end='')
  
  