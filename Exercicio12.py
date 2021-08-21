preco = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor de desconto: %'))
print(f'Considerando {desconto}% de desconto, o preço do produto passa a ser {preco*((100-desconto)/100)}')