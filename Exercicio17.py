from math import hypot
catopo = float(input('Digite o Cateto Oposto: '))
catadj = float(input('Digite o Cateto Adjacente: '))
print(f'A hypotenusa do cateto oposto {round(catopo,2)} e do cateto adjancente {round(catadj,2)}, e igual a {round(hypot(catopo, catadj),2)}')