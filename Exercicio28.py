from random import randint, randrange
from time import sleep
n = int(input("Qual o numero? "))
numSorteado = randrange(5)
print('PROCESSANDO...')
sleep(2)
print(f'Você Ganhou!') if n == numSorteado else print(f'Você Perdeu!')