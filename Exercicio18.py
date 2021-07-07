from math import cos, sin, tan, pi
angulo = float(input('Digite o Valor de um angulo: '))
print(f'O Angulo {angulo}, possui os seguintes valores para seno, cosseno e Tangetente respectivamente')
print(f'seno = {sin(angulo*(pi/180))}\ncosseno = {cos(angulo*(pi/180))}\ntangente = {tan(angulo*(pi/180))}')
