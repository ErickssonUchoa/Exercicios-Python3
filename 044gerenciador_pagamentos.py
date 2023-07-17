print('\033[0;32;40m-='*15)
print('\033[0;31;40mIMC v2.0')
print('\033[0;32;40m-='*15)

valor = float(input('Informe o valor do produto: '))
opcao = input("""
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
""")

if opcao == '1':
    total = valor - (valor * 0.10)
    desconto = valor * 0.10
    print(f'O valor final do produto com desconto de {desconto:.2f} R$ é {total:.2f} R$')
elif opcao == '2':
    total = valor - (valor * 0.05)
    desconto = valor * 0.05
    print(f'O valor final do produto com desconto de {desconto:.2f} R$ é {total:.2f} R$')
elif opcao == '3':
    print(f'O valor final do produto sem alterações é {valor:.2f} R$')
else:
    parcela = int(input('Quantas parcelas? '))
    total = valor + (valor * 0.20)
    juros = total / parcela
    print(f'O valor do produto parcelado em {parcela}x de {juros:.2f} R$ ', end=''
          f'será de {total:.2f} R$')
