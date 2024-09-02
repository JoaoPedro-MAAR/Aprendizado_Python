n = int(input('Digite quantas pesssoas tem: '))
homens = 0
mulheres = 0
for _k in range(1,n+1):
  sexo = input('Qual o seu sexo, M ou F: ').upper()
  if sexo == 'M':
    homens = homens + 1 
  elif sexo == 'F':
    mulheres = mulheres + 1
  else:
    print('Valor invalido')
print(f'Tem {homens} homens, e {mulheres} mulheres')
porcentagem_M = (homens / n)*100
porcentagem_F = (mulheres / n)*100
print(f'Tem {porcentagem_M}% de homens e {porcentagem_F}% de mulheres')