frase = input('Digite a frase: ')
rep = int(input('quantas repetições: '))
frase_rep = ''
for i in range(len(frase)):
  if frase[i] in 'aAeEiIoOuU':
    frase_rep +=  frase[i] * rep
  else:
    frase_rep += frase[i]
print(frase_rep)
  