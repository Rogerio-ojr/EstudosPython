nome = input('Digite um nome: ')
nome = nome.strip()
for i in nome.split():
    a = i
print(f'O primeiro nome e {nome.split()[0]}, e o Ultimo nome e {a}')
