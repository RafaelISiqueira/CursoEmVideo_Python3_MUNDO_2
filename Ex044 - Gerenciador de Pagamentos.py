#Calcular o valor a ser pago por um produto, considerando, preço normal e condição de pagamento:
#À vista dinheiro: 10% desconto
#Á vista cartão: 5% desconto
#Em 2x no cartão: preço normal
#Em 3x ou mais: 20% juros

#FIRULA
print('{:=^40}'.format(" BAZAR DO ZERO "))

#1°: preço dos produtos:
preço = float(input("Preço total das compras:R$ "))

#2°: Print das opções de pagamento:
print('''FORMAS DE PAGAMENTO
[ 1 ] À VISTA no Dinheiro
[ 2 ] À VISTA no Cartão
[ 3 ] Em 2x no Cartão
[ 4 ] Em 3x ou mais''')

#3°: Digitar uma das opções acima:
opção = int(input("Escolha uma das Opções de pagamento: "))

#4°: If, Elif e Else (Calculo de porcentagem para descontos e juros):
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela_2x = total / 2
    print("Sua compra será parcelada em 2x no valor de R${:.2f} (SEM JUROS)".format(parcela_2x))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    parcela_3x = total / 3
    print("Sua compra vai ser parcelada em 3x no valor de R${:.2f} (COM JUROS DE 20%)".format(parcela_3x))
else:
    print("Opção INVÁLIDA. Tente novamente.")
print("Sua compra de R${:.2f} Vai custar com desconto R${:.2f}".format(preço, total))
print("Obrigado pela preferencia, volte sempre")

