from datetime import date
anoNasc = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year
diferenca = anoAtual - anoNasc
print(f'O ano de nascimento de {anoNasc}')
print(f'Quem nasceu em {anoNasc}, tem {diferenca} anos em {anoAtual}')
if diferenca == 18:
    print('Você de se alistar IMEDIATAMENTE!')
elif diferenca < 18:
    print(f'O ano do seu alistamento deverá ser em {anoNasc + 18}')
else:
    print(f'O ano do seu alistamento Foi em {anoNasc + 18}')
