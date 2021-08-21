vrCasa = float(input('Qual o Valor da Casa? R$'))
salario = float(input('Qual o seu salario? R$'))
anos = float(input('Em quantos anos deseja pagar? '))
prestacao = vrCasa / (anos * 12)
print('Para um casa no valor de R${:.2f} em {} anos '.format(vrCasa, anos), end='')
print('Você terá uma prestação no valor de R&{:.2f}'.format(prestacao))
if vrCasa / (anos * 12) <= (salario * 0.3):
    print('SEU EMPRESTIMO FOI APROVADO!!!')
else:
    print('Como a prestação de R${:.2f}, ultrapassa o limite de 30% da sua renda de R${:.2f}'.format(prestacao, salario))
    print('SEU EMPRESTIMO FOI NEGADO!!!')


