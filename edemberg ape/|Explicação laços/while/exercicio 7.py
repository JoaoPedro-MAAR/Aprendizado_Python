
quantos = int(input('Quantos serao os participantes: '))
idade = int(input('Digite sua idade: '))
count = 0 
Entre18e21 = 0
menor = 99999999999999999

numerador = 0
while idade != 0 and count < quantos:
  if idade < menor:
    menor = idade 
  if idade >= 18 and idade <= 21:
    Entre18e21 += 1
  numerador = idade + numerador
  idade = int(input('Digite sua idade: '))
  count += 1
Porcentagem = (Entre18e21*100)/quantos
media = numerador / quantos
print(f'A media do publico era {media}')
print(f'A porcentagem é {Porcentagem} ')
print(f'O mais novo tem {menor} anos')

    
    
  
  