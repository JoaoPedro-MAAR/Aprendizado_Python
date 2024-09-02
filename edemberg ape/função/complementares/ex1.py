def media(n1,n2,n3):
  soma = n1 + n2 + n3
  media = soma/3
  return media
def ABC(media):
 
  if media < 4:
    conceito = 'C'
  elif media < 8 :
    conceito = 'B'
  else:
    conceito = 'A'
  return conceito
n1 = int(input('Digite sua primeira nota: '))
n2 = int(input('Digite sua primeira nota: '))
n3 = int(input('Digite a terceira nota: '))
print(ABC(media(n1,n2,n3)))
