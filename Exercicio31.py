distancia = float(input('Qual a distancia da viagem? ').replace(",","."))
v = f'{(distancia * 0.5):_.2f}'
v = v.replace(".",",").replace("_",".")

f = f'{(distancia * 0.45):_.2f}'
f = f.replace(".",",").replace("_",".")

if distancia <= 200:
    print(f'O Preco da passagem e de R${v}.')
else:
    print(f'O Preco da passagem e de R${f}.')
