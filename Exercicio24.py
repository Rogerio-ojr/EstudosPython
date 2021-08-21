cidade = input('Digite o nome da cidade: ').strip()

if cidade.lower().split()[0] == "santo":
    analise = "A Cidade começa com a palavra Santo"
else:
    analise = "A Cidade nao começa com a palavra Santo"

print(analise)
