hora_inico = int(input('Qual hora o jogo começou: '))
hora_final = int(input('QUal hora o jogo terminou: '))
if hora_inico > hora_final:
  h = 24 - (hora_inico - hora_final)
  print(f'O jogo durou {h} horas') 
elif hora_inico < hora_final:
  h = hora_final - hora_inico
  print(f'O jogo durou {h} horas')
else:
  print('O jogo durou 0 horas')
  
  