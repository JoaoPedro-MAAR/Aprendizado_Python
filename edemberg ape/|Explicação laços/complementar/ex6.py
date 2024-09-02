SENHA_CORRETA = "abcd"
count = 0
while count<3:
  senha = input('Digite a senha: ')
  count += 1
  if senha == SENHA_CORRETA: 
    print('Parabens voce esta logado')
    break
  if senha != SENHA_CORRETA:
    print('Senha errada')
    continue
print('Excedeu suas tentativas')
    