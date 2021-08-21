v = input('Digite seu Primerio nome e sua idade: ')
v2 = ''
if v.isnumeric() == True:
    v2 = 'numerico\n'
if v.isalpha() == True:
    v2 = v2 + 'Alpha\n'
if v.isalnum() == True:
    v2 = v2 + 'Alpha numerico\n'
if v.islower() == True:
    v2 = v2 + 'Possui Letras Minusculas\n'
if v.isupper() == True:
    v2 = v2 + 'Possui Letras Maisculas\n'
if v.istitle() == True:
    v2 = v2 + 'Esta Capitalizada\n'
if v.isspace() == True:
    v2 = v2 + 'Possui Espaços\n'

print(f'O Tipo primitivo dessa variavel e {type(v)}, e a mesma possui a seguintes caracteristicas:\n {v2}')
