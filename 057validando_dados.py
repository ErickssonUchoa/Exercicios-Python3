print('\033[0;32;40m-='*15)
print('\033[0;31;40mValidação de Dados')
print('\033[0;32;40m-='*15)

while True:
    s = input('Qual o seu sexo? [M]/[F]: ').upper().strip()[0]  # Pegando a primeira letra se for digitado masculino.
    if s != 'M' and s != 'F':
        print('Sexo inválido, digite novamente')
    if s == 'M':
        print('Sexo Masculino Registrado.')
        break
    if s == 'F':
        print('Sexo Feminino Registrado.')
        break
print('Programa Finalizado!')

# sexo = input('Digite seu sexo [M]/[F]: ')
# while sexo not in 'MmFf':
#     sexo = input(f'Dados inválidos, Digite novamente seu sexo [M]/[F]:').strip().upper()[0]
# print(f'O sexo {sexo} Foi Registrado')
