
'''
cont = 1 
while cont < 11:
   print('IFPB')
   cont += 1

'''
'''
cont = 1
while cont < 51:
  print(cont)
  cont += 1
'''

''''
n = int(input('Digite quantas vezes voce quer testar :'))
cont = 1
while cont <= n:
  n2 = int(input('Qual o numero vocẽ quer testar: '))
  if n2%2 == 0:
    print('Par')
  else:
    print('Impar')
  cont += 1
  '''
"""
n = int(input('Digite quantas vezes voce quer testar :'))
cont = 1
n2 = 1
if n != 0:
  while cont <= n and n2!=0:
    n2 = int(input('Qual numero você quer o dobro : '))
    cont += 1
    if n2 != 0:
      print(n2 * 2)
    else:
      print(' 0 nao pode ser dobrado')
else:
  print('Vocẽ selecuonou zero')
"""
n = int(input('Digite quantas vezes voce quer testar :'))
cont = 1
n2 = 1
soma = 0
s = 0
if n != 0:
  while cont <= n and n2!=0 and soma <=100 and s == 0 :
    n2 = int(input('Digite um numero : '))
    cont += 1
    if soma + n2 <= 100:
      soma = soma + n2
      if n2 != 0:
          print(n2)
      else:
          print(' 0 é invalido')
          s = 1
    else: 
      print(f'A soma excedeu 100,esta agora em {soma + n2}')
      s = 1
else:
  print('Vocẽ selecionou zero')
print(f'A soma sem o utlimo numero sera: {soma}')