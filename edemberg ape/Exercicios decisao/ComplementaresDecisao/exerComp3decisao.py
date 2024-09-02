ano = int(input('Digite um ano: '))
if ano%4 == 0 and ano%100 != 0: 
  print('O ano é bissexto')
elif ano%400 == 0:
  print('O ano é bissexto')
else:
  print('O ano não é bisssexto')
#Pode se resumir o if e elif fazendo uma operação so sendo if (ano%4 == 0 and ano% != 0) or (ano%400 == 0 ): 