from datetime import date
anoNasc = int(input('Digite o ano de Nascimento do Atleta: '))
anoAtual = date.today().year
diferenca = anoAtual - anoNasc
if diferenca > 0 and diferenca <= 9:
    print('Categoria MIRIN')
elif diferenca > 9 and diferenca <= 14:
    print('Categoria INFANTIL')
elif diferenca > 14 and diferenca <= 19:
    print('Categoria JUNIOR')
elif diferenca > 19 and diferenca <= 20:
    print('Categoria SENIOR')
elif diferenca > 20:
    print('Categoria MASTER')
else:
    print('O Ano {} e maior do que o ano atual {}, portanto o mesmo não se enquandra em nenhuma categoria'.format(anoNasc, anoAtual))
