def vogal(frase):
  global count
  count = 0
  for i in range(len(frase)):
    if frase[i] in 'AaeEIioOUu':
      count += 1
    else:
      count += 0
  return count > 0
  


frase = input('Frase: ')
print(vogal(frase))
print(f'Essa palavra tem {count} vogais')
    