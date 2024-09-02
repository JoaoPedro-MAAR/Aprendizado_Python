print("Aqui sera mostrado uma fucionalidade de uma calculadora,para isso precisaremos que você: ")
n1 = int(input("Diga um numero para ser calculado: "))
n2 = int(input('Digite outro numero: '))
operador = input('Diga qual operando sera utilizado,como +,-,*,/,%: ')

if (operador == '+' or operador == 'soma' or operador == 'adição' ):
    resultado = n1 + n2
    print(f'O resultado de {n1} {operador} {n2} é {resultado}: ')
elif (operador in ('menos,-,subtração')):
    resultado = n1 - n2
    print(f'O resultado de {n1} {operador} {n2} é {resultado}: ')
elif (operador in ('vezes','*','multiplicação')):
    resultado = n1 * n2
    print(f'O resultado de {n1} {operador} {n2} é {resultado}: ')
elif (operador in ('divisão','dividir','/')):
    if n2 != 0:
      resultado = n1 / n2
      print(f'O resultado de {n1} {operador} {n2} é {resultado}: ')
    else:
      print("O segundo operador nao pode ser zero na divisão ")
elif (operador in ('resto','%')):
    if n2 != 0:
      resultado = n1 % n2
      print(f'O resultado de {n1} {operador} {n2} é {resultado}: ')
    else:
      print("O segundo operador nao pode ser zero no resto pois ele é uma divisão ")
else:
  print('Operador invalido ')
  