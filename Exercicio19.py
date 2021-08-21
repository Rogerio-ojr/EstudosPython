import random
from math import trunc
alunos = ['Rogerio Maciel de Oliveira Junior','Elias Antonio Rodrigues','Marcio Junio Rodrigues','Gilberto Moura Silveira']
print(f'O aluno sorteado para apagar o guadro e {alunos[trunc(random.uniform(0,len(alunos)))]}')