#from random import randint
#nrInt = randint(1,1000)
nrInt = int(input('Esolha um numero inteiro: '))
print('''Digite a opção que deseja converter o numero:
      [ 1 ] Converter para Binario
      [ 2 ] Converter para hexadecimal
      [ 3 ] Converter para Octal''')

opcao = int(input('Digite a opção: '))
if opcao == 1:
    print('A conversão de {}, para Binario e de {}'.format(nrInt, bin(nrInt)[2:]))
elif opcao == 2:
    print('A conversão de {}, para hexadecimal e de {}'.format(nrInt, hex(nrInt)[2:]))
elif opcao == 3:
    print('A conversão de {}, para Octal e de {}'.format(nrInt, oct(nrInt)[2:]))
else:
    print('Você Selecinou opção incorreta, digite apenas um numero de 1 a 3')
