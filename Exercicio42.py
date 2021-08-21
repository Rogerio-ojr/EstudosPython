import Exercicio35
if Exercicio35.Triangulo(Exercicio35.a, Exercicio35.b, Exercicio35.c) == 1:
    if Exercicio35.a == Exercicio35.b == Exercicio35.c:
        print('E um triangulo do Tipo Equilatero')
    elif Exercicio35.a != Exercicio35.b != Exercicio35.c != Exercicio35.a:
        print('E um triangulo do Tipo Escaleno')
    elif (Exercicio35.a == Exercicio35.b) or (Exercicio35.b == Exercicio35.c) or (Exercicio35.a == Exercicio35.c):
        print('E um triangulo do Tipo isoceles')
else:
    print('Não foi possivel Identificar nenhum tipo de Triângulo')

