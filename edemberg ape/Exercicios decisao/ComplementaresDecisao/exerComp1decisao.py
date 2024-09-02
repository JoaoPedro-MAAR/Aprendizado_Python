print(
    'Exercicio na qual sera disponibilizado um numero de 1 à 7 para o usuário escolher,sendo 1 domingo,2 segundo e por assim em diante,afim de mostrar se é dia util ou nao'
)
dia = input('Digite um numero: ')

if (dia == '1'):
  print('Domingo nao é um dia util')
elif (dia == '7'):
  print('Sabado não é um dia util')
elif (dia == '2'):
  print('Segunda é um dia util')
elif (dia == '3'):
  print('Terça é um dia util')
elif (dia == '4'):
  print('Quarta é um dia util')
elif (dia == '5'):
  print('Quinta é um dia util')
elif (dia == '6'):
  print('Sexta é um dia util')
else:
  print('O numero que voce colocou nao corresponde a nenhum dia da semana')
