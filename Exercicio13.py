salario = float(input('Qual o seu Salario? R$'))
reajuste = float(input('Qual o valor do reajuste: '))
print(f'Considerando {reajuste}% de reajuste, o novo salario e de {round(salario + ((salario*reajuste)/100),2)}')