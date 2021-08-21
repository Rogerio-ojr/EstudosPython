from datetime import date
ano = input('Digite o Ano, ou coloque 0 para o ano atual: ')

#Avalia se o ano e bissexto caso coloque 0
if int(ano) == 0:
    ano = date.today().year
    if ano % 4 == 0 or ano % 100 == 0 and ano % 400 == 0:
        print(f'O ano {ano}, e um ano Bissexto')
    else:
        print(f'O ano {ano}, não e um ano Bissexto')
#Caso nao coloque 0, ele trata o input, para que na possibilidade de colocar virgula no ano, o programa não aceite, tal input.
else:
    if ano.find(',') > 0:
        print('Favor Digitar o ano sem a virgula')
    else:
        ano = int(ano)
        if ano % 4 == 0 or ano % 100 == 0 and ano % 400 == 0:
            print(f'O ano {ano}, e um ano Bissexto')
        else:
            print(f'O ano {ano}, não e um ano Bissexto')