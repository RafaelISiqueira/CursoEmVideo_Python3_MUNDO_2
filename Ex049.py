#Faça a Tabuada do Ex009, Usando um Laço for.

#1°: Valor do número inteiro:
num = int(input("Digite um número para ver sua Tabuada: "))

#2°: Usando Laço for:
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
