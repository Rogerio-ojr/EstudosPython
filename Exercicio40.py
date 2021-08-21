nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
listNotas = [nota1, nota2]
contador = 0
for i in listNotas:
    contador +=1
media = (nota1 + nota2) / contador
if  media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO!!!')

