peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)
print('O seu IMC e de {:.2F}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Você está com Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MORBIDA')