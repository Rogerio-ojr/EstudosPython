velocidade = input("Qual a velocidade? ")
if int(velocidade) > 80:
    print(f'A sua velocidade de {velocidade}km/h, esta lhe gerando uma multa no valor de R${(int(velocidade)-80)*7}')
else:
    print(f'Você esta dentro do limite da via.')