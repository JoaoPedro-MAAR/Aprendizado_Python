"""(obs: N será lido).
3. O algoritmo de Euclides para determinar o MDC entre dois números inteiros
consiste em formar uma sequência de inteiros cujos dois primeiros
elementos são os números dados. Cada elemento seguinte é o resto da
divisão dos dois anteriores. A sequência terminará quando um elemento dela
for nulo. O MDC entre os números dados é o elemento anterior ao zero. Faça
uma implementação deste programa.
Ex: Dados os números 12 e 15, será formada a sequência: 12, 15, 12, 3, 0 e o
MDC entre 12 e 15 é 3."""

n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
proximo = 1
while True:
  if n1%n2==0:
    print('O maximo divisor comun é ', n2)
    continue
  if n1%n2!=0:
    aux = n1
    n2 = n1
    n2 = aux
    proximo = n1%n2
    n2 = proximo
    print(n2)
    break
    
    
  