'''6. Na primeira etapa de um concurso, o candidato tem que fazer duas provas. Dessas duas notas é
tirada a média do candidato. Caso essa média seja maior ou igual a 7.0, ele estará apto a fazer a
segunda etapa do concurso. Na segunda etapa, ele fará mais uma prova, onde deverá obter uma
nota maior ou igual a 8.0 para ser aprovado no concurso.
Escreva um programa que leia as notas da primeira etapa, calcule a média da primeira etapa, e
se o candidato for aprovado na primeira etapa, leia a nota dele na segunda etapa e diga se ele
foi aprovado ou não no concurso.'''

n1etapa1 = float(input('Digite a nota da primeira prova do candidato: '))
n2etapa1 = float(input('Digite a nota da segunda prova do candidato: '))
media12etapa = (n1etapa1 + n2etapa1)/2
if (media12etapa < 7):
  print(f'Voce foi reprovado na primeira etapa com uma media {media12etapa}')
else:
  print(f'Parabens voce foi aprovado na primeira etapa com uma media de  {media12etapa}')
  notaetapa2 = float(input('Digite quanto voce tirou na prova da segunda etapa: '))
  if (notaetapa2 >= 8):
    print('Parabéns voce passou!!!!!!')
  else:
    print('Que pena você nao foi aprovado')