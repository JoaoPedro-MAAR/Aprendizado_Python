def clas_menor(n1,n2,n3):
  menor = n1
  if n1 < menor:
    menor = n1
  elif n2 < menor:
    menor = n1
  elif n3 < menor:
    menor = n3
  print('O menor é' , menor)
  #Poderia ter sido usado a função return menor
n1 = int(input('Digite o numero: '))
n2 = int(input('Digite o numero: '))
n3 = int(input('Digite o numero: '))
clas_menor(n1,n2,n3)