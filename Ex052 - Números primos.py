#Progama que leia um número inteiro e diga se ele é ou não PRIMO

#1°: Valor inteiro e Total:
num = int(input("Dígite um numero: "))
total = 0

#2°: Laços para calculo de números primos:
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end='') # Letra Amarela
        total += 1
    else:
        print("\033[31m", end='') # Letra Vermelha
    print("{} ".format(c), end='')
print("\n\033[mO número {} foi divisível {} vezes".format(num, total))

#3°: If e else para mostrar Se é PRIMO OU NÂO (numeros primos são números apenas divisiveis por 1 e ele mesmo)
if total == 2:
    print("E por isso que ele é um número PRIMO!")
else:
    print("E por isso ele NÃO é um NÚMERO PRIMO")