vrNormalProduto = input('Digite o Valor normal do Produto: R$')
vrNormalProduto = float(vrNormalProduto.replace(',','.'))
dinChequeVista = round(vrNormalProduto * 0.9, 2)
cartaoVista = round(vrNormalProduto * 0.95, 2)
cartaoParcelado2 = vrNormalProduto
cartaoParcelado3ouMais = round(vrNormalProduto * 1.2, 2)
print('''Selecione a forma de Pagamento.
      [ 1 ] Dinheiro ou no cheque a Vista:
      [ 2 ] Cartão a Vista:
      [ 3 ] Em até 2 vezes no cartão:
      [ 4 ] Acima de 3 Vezes no Cartão: 
      ''')
opcao = int(input('Selecione, conforme acima a sua forma de pagamento: '))

if opcao == 1:
    print(f'O Valor do produto e de R${vrNormalProduto} e no Dinheiro ou no Cheque você possui 10% de desconto, e o valor total fica em R${dinChequeVista}')
elif opcao == 2:
    print(f'O Valor do produto e de R${vrNormalProduto} e no Cartão a vista, você possui 5% de desconto, e o valor total fica em R${cartaoVista}')
elif opcao == 3:
    print(f'O Valor do produto e de R${vrNormalProduto} e parcelado de até duas vezes não possui desconto')
elif opcao == 4:
    print(f'O Valor do produto e de R${vrNormalProduto} e parcelado acima de 2 vezes tera um acrescimo de 20% de juros, ficando o valor total de R${cartaoParcelado3ouMais}')
else:
    print('Por favor digite um valor somente de 1 a 4')
