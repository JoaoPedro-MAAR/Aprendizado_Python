'''Faça um programa que calcule e mostre o fatorial de um número N, fornecido
pelo usuário. A definição de fatorial é mostrada a seguir'''

n = int(input('Digite um numero: '))
fatorial = 1
for k in range(1 , n + 1):
 fatorial = k * fatorial
print(fatorial)