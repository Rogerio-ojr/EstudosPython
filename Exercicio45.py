from random import randint
from time import sleep
computador = randint(1,3)
print('''Selecione a sua Opção: 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
''')
usuario = int(input('Qual você quer jogar 1, 2 ou 3? '))
escolhaComputador = 'Pedra' if computador == 1 else 'Papel' if computador == 2 else 'Tesoura'
escolhaUsuario = 'Pedra' if usuario == 1 else 'Papel' if usuario == 2 else 'Tesoura'
print('---------------//---------------')

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')

print('---------------//---------------')

if usuario == 1 and computador == 2:
    print(f'Você perdeu, Papel Mata Pedra')

elif usuario == 2 and computador == 3:
    print(f'Você perdeu, Tesoura Mata Papel')

elif usuario == 3 and computador == 1:
    print(f'Você perdeu, Pedra Mata tesoura')

elif usuario == 2 and computador == 1:
    print(f'Você Ganhou, Papel Mata Pedra')

elif usuario == 3 and computador == 2:
    print(f'Você Ganhou, Tesoura Mata Papel')

elif usuario == 1 and computador == 3:
    print(f'Você Ganhou, Pedra Mata tesoura')

elif usuario == computador:
    print(f'Empate as escolha do Usuario: {escolhaUsuario}, foi igual do computador de: {escolhaComputador}')