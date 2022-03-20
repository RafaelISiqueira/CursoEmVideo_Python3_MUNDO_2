#Criar uma progressão aritimética:

#1°: criar o Termo e a Razão:
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))

#2°: Calculo do Décimo termo de uma PA:
décimo = primeiro + (10 - 1) * razão

#3°: Laço para Calculo:
for c in range(primeiro, décimo + razão, razão):
    print("{} ".format(c), end="-> ")

#4°: Printe para Encerramento:
print("ACABOU")