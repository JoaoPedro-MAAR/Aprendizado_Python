frase = input('digite a frase: ').lower()
frase_criptografada = ''
for i in range(len(frase)):
  if frase[i] == 'a':
    frase_criptografada += ' '
  elif frase[i] == 'e':
    frase_criptografada += 'u'
  elif frase[i] == 'i':
    frase_criptografada += 'o'
  elif frase[i] == 'o':
    frase_criptografada += 'i'
  elif frase[i] == 'u':
    frase_criptografada += 'e'
  elif frase[i] == ' ':
    frase_criptografada += 'a'
  else:
    frase_criptografada += frase[i]
print(frase)
print(frase_criptografada)
    