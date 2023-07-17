print('\033[0;32;40m-='*15)
print('\033[0;31;40mIMC v2.0')
print('\033[0;32;40m-='*15)

nome = input('Informe seu nome seu nome: ')
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Olá {nome}, seu imc é {imc:.2f} e você está abaixo do peso.')
elif imc <= 25:
    print(f'Olá {nome}, seu imc é {imc:.2f} e você está no peso ideal.')
elif imc <= 30:
    print(f'Olá {nome}, seu imc é {imc:.2f} e você está em sobrepeso.')
elif imc <= 40:
    print(f'Olá {nome}, seu imc é {imc:.2f} e você está em obesidade.')
else:
    print(f'Olá {nome}, seu imc é {imc:.2f} e você está em obesidade mórbida.')
