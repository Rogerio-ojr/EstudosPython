nome = input('Digite um nome: ').strip()
if nome.upper().count('SILVA') > 0:
    analise = 'sim'
else:
    analise = 'nao'
print(analise.capitalize())