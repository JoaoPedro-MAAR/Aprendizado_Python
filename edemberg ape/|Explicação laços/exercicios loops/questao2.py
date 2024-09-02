"""Faça um programa que leia um número N, inteiro, e some todos os números
de 1 até N, mostrando o resultado."""

n = int(input('Digite um numero: '))
soma = 0 
for k in range(1 , n + 1):
 soma = k + soma
print(soma)