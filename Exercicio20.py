import random
from math import trunc
alunos = ['Rogerio Maciel de Oliveira Junior','Elias Antonio Rodrigues','Marcio Junio Rodrigues',
          'Gilberto Moura Silveira','Rogerio de Oliveira Silva','Aluno Teste 2','Aluno teste 4','Aluno teste 5','Aluno teste 6']
trabalho = {}
for n in alunos:
    while True:
        numerosorteado = trunc(random.uniform(0, len(alunos)))
        if numerosorteado not in trabalho.keys():
            trabalho[numerosorteado] = n
            break
contador = 0
print('A ordem da apresentação do Trabalho será a seguinte: ')
for i in trabalho:
    print(f'{contador+1}º - {trabalho[contador]}')
    contador+=1


