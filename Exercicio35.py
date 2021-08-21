a = int(input('Digite o comprimento do lado a: '))
b = int(input('Digite o comprimento do lado a: '))
c = int(input('Digite o comprimento do lado a: '))

def Triangulo(a, b, c):
    return 1 if a<b+c and b<a+c and c<b+a else 0

if a<b+c and b<a+c and c<b+a:
    print(f'As retas {a}, {b} e {c}, Sim formam um triângulo')
else:
    print(f'As retas {a}, {b} e {c}, Não formam um triângulo')
