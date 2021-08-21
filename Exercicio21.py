import os
DIR = os.path.join('C:\\','users','roger','Documents','Projetos Python')
os.chdir(DIR)
print(os.listdir())
#with os.open('Ceremonya - Na língua dos anjos_50k.mp3', os.O_RDWR) as o:
#    os.get_exec_path(o)
with open("Ceremonya - Na língua dos anjos_50k.mp3", "r") as o:
    os.open(o, os.O_RDWR)
#  f.write("Testando escrita com with")