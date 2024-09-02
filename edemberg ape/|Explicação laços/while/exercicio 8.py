''' 8. O cardápio de uma casa de lanches, especializada em sanduíches, é dado a
seguir.
CÓDIGO NOME PREÇO
H Hamburger R$ 5,00
C Cheese Burger R$ 6,00
B Cheese Bacon R$ 7,00
F Cheese Frango R$ 4,00

Faça um programa que leia o código e a quantidade de cada item comprado
por um cliente (a leitura do código “X” indica o fim dos dados de entrada). Ao
final, calcule e exiba o total a pagar.
Veja o exemplo abaixo, considerando que o cliente pediu 3 Hamburger e 2
Cheese Bacon:
Entrada:
Código: H
Quantidade: 3
Código: B
Quantidade: 2
Código: X
Saída:
Total a pagar: R$ 29.00'''

pedido = ""
valor = 0
H = 5
C = 6
B = 7
F = 4
while pedido != "X":
  pedido = input('Diga qual sera o codigo do seu pedido: ').upper()
  if pedido != "X":
    qntd = int(input('Qual a quantidade desejada: '))
    if pedido == "H":
      valor = (H * qntd) + valor
    elif pedido == "C":
      valor = (C * qntd) + valor
    elif pedido == "B":
      valor = (B * qntd) + valor
    elif pedido == "F":
      valor = (F * qntd) + valor

    else:
      print('Operador invalido caso queira terminar a operação digite X ')
  else:
    break
print(f'O valor de seu pedido sera {valor},00 reais')
   

  