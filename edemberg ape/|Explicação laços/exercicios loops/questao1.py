'''Faça um programa que calcule e mostre os números múltiplos de 5 do
intervalo 50 a 300, juntamente com suas raízes e seus cubos.'''

import math

for multiplos in range(50 , 301 , 5):
  print(multiplos)
  print(f'Cubo é {multiplos ** 3}')
  raiz = math.sqrt(multiplos)
  numero_2casas = "{:.2f}".format(raiz)
  print(f'Raiz é {numero_2casas}')