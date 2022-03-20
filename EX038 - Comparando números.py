#ler 2 números inteiros e mostrar a mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#OU os dois são iguais.

#1°: Digitar o 1°,2° Números
n1 = int(input('Digite aqui, O PRIMEIRO Número: '))
n2 = int(input('Digite aqui, O SEGUNDO Número: '))

#2°: If, Elif e else
if n1 > n2:
    print("O PRIMEIRO valor é maior")
elif n1 < n2:
    print("O SEGUNDO VALOR é maior")
else:
    print("Os dois números sao IGUAIS")
