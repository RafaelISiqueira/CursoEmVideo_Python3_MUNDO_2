#leia 6 números inteiros e mostre somente a soma dos números pares:

#1°: Atribuir soma e contador:
soma = 0
contador = 0

#2°: escrever 6 numeros, somar os pares, ou seja, divisiveis por 2:
for c in range(1,7):
    num = int(input("Digite o {}° Valor: ".format(c)))
    if num % 2 == 0:
        soma += num
        contador += 1

#3°: printar o resultado
print("Você informou {} números PARES e a soma foi {}".format(contador, soma))