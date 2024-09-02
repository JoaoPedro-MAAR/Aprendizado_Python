maior = -9999999999999
menor = 99999999999
count = 1
dia_quente = dia_frio = 1
while count<7:
  temp = float(input('Digite a temperatura: '))

  if temp > maior:
    maior = temp
    dia_quente = count
  if temp < menor:
    menor = temp
    dia_frio = count
  count += 1
print(f'O dia mais quente foi o dia {dia_quente} com uma temperatura de {maior}')
print(f'O dia mais frio foi  o dia {dia_frio} com uma temperatura de {menor}')