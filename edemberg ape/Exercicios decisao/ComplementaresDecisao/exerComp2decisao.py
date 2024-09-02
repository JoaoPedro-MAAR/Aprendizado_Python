caractere = input('Digite um caractere: ').upper()

if (caractere in ('A,E,I,O,U')):
  print('Isso é uma vogal:')
elif (caractere in ('B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z')):
  print('É uma consoante')
elif caractere in '0123456789':
  print('E um numero')
else:
  print('É uma caractere especial')