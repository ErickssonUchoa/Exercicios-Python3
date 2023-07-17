horario = int(input('Informe o horário: '))

if horario < 0 or horario > 23:
    print('Informe um horário válido!')
else:
    if horario >= 0 and horario <= 11:
        print('Boa dia!')

    elif horario >= 12 and horario <= 17:
        print('Boa Tarde!')

    else:
        print('Boa Noite!')
