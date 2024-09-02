


def idententidade(matriz):
  furo = 0
  for i in range(LINHA):
    for j in range(LINHA):
      if i == j:
        if matriz[i][j] == 1:
          furo +=0
          
        else:
          furo += 1
          
      else:
        if matriz[i][j] != 0:
          furo += 1
         
        else:
          furo += 0
  if furo == 0:
    
    return True
  else:

    return False
        
          

LINHA = int(input('Quantas linhas: '))

m1 = [None] * LINHA
for i in range(LINHA):
  m1[i] = [None] * LINHA
  for j in range(LINHA):
    m1[i][j] = int(input('Digite uma valor: '))

idententidade(m1)
if idententidade(m1) :
  print('É identidade')
else:
  print('Não é identidade')

      