n = int(input('Digite um valor: '))
y = int(input('Digite um valor final: '))
x = int(input('Digite um valor inicial : '))

for i in range(x,y + 1):
 if i%n==0:
  print(f'{i}, ' , end='')