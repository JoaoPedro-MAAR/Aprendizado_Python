n = int(input('Digite o tamanho do vetor: '))
vetor = [None]*n
vetor_b = [None]
lista = []
k = int(input('Qual valor você quer procurar: '))
cont_2 = 0 
cont= -1
posissao = 0
for i in range(n):
  vetor[i] = int(input(f'Digite o {i + 1} valor'))
  cont += 1 
  if vetor[i] == k:
    cont_2 += 1
    posissao = cont
    
    print(f'K apareceu na {posissao} posição ')
