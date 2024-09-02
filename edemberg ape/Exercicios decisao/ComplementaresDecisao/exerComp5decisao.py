import math

a = float(input('Digite o valor de A na equação: '))
b = float(input('Digite o valor de B na equação: '))
c = float(input('Digite bo valor de C na equação: '))
if (a != 0 ):
  delta = (b ** 2) -4 * a * c
  print(f'Delta é: {delta}')
  if (delta > 0 ):
      raiz = math.sqrt(delta)
      print(f'A raiz de delta é {raiz}')
      x1 = (-b + raiz)/ (2 * a)
      X2 = (-b - raiz) / (2 * a)
      print(f'As raizes da equaçao sao {x1} e {x2}')
  elif (delta == 0 ):
      x = -b / (2 * a)
      print(f'A raiz da equação é: {x}')
  else:
      print('Nao tem raiz, pois delta menor que zero nao fornece raiz ')
else:
    print('Não é uma equação de segundo graus')