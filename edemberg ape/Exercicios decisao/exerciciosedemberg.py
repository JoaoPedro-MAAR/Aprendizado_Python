peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros: '))
altura2 = altura ** 2
imc = peso/altura2
print(f'Com um imc de {imc:.2f} voce esta classificado como:',end='')
if imc < 18.5:
    print('Abaixo do peso normal')
elif imc >= 18.5 and imc < 24.9:
    print('Peso normal ')
elif imc >= 25.0 and imc < 29.9:
    print('Acima do peso')
elif imc >= 30.0 and imc < 34.9:
    print('Obsidade classe 1')
elif imc >= 35.0 and imc < 39.9:
    print('Obsidade em classe 2')
else:
    print("Obesidade classe 3")