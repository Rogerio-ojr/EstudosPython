salario = input('Qual o seu salario? ').replace(",",".")
salario = float(salario)

if salario > 1250:
    salario = salario * 1.10
else:
    salario = salario * 1.15

salario = f'{salario:_.2f}'
salario = salario.replace(".",",").replace("_",".")

print(f'Seu novo salário e de R${salario}')
