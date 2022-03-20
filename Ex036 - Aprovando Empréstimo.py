#Aprovar emprestimo bancário, Perguntar valor da casa, Salário do comprador, quantos anos ele vai pagar
#Calcular a prestação mensal, não pode excer 30% do salário, se não é negado.

#1°:Atribuir valores para Casa, salário e anos:
casa = float(input("Digite, O VALOR da casa: R$"))
salário = float(input("Digite, O seu SALÁRIO: R$"))
anos = int(input("Digite, Quantos anos de FINANCIAMENTO?: "))

#2°: Calculo para a prestação e o Minímo:
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100

#3°: Print das mensagens de conclusão:
print('Para pagar uma casa de R${:.2f} em {} anos, '.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prestação))

#4°:IF e Else:
if prestação <= mínimo:
    print("Emprestimo Pode ser CONCEDIDO!")
else:
    print("emprestimo NEGADO!")
