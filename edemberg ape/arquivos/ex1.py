'''

1. Escreva um programa que exiba na tela um arquivo texto cujo nome será lido pelo
teclado.

'''
nome_arquivo = input('Qual o nome do arquivo')
ex1_2 = open(f"edemberg ape/arquivos/{nome_arquivo}.txt","w")
ex1_2.write('Juan Pablo Escobar\n')
ex1_2.write('Javier Escuella\n')
ex1_2.write('Moreira\n')
ex1_2.close()

ex1 = open(f"edemberg ape/arquivos/{nome_arquivo}.txt","r")
for i in range(3):
  print(ex1.readline())

