texto = input('Digite um nome: ').strip()
print(f'O texto "{texto}" possui {texto.lower().count("a")} caracteres a')
print(f'A letra "a" aparece a primeira vez na posição {texto.lower().find("a")+1}')

contador = 0
for i in list(texto.lower()):
    if i == "a":
        analise = contador
    contador += 1
print(f'A ultima posição da letra "a" e {analise+1}')

print(f'A ultima posição da letra "a" e {texto.lower().rfind("a")+1}')