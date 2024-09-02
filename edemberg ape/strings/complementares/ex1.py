email = input('Digite seu email: ')
for i in range(len(email)):
  if email[i] != '@':
    print(email[i])
  else:
    