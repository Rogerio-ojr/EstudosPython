n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 > n2:
    print('O primeiro numero {}, e maior do que o segundo numero {}'.format(n1, n2))
elif n1 < n2:
    print('O primeiro numero {}, e menor do que o segundo numero {}'.format(n1, n2))
else:
    print('Os dois numeros {} e {}, são iguais'.format(n1, n2))
