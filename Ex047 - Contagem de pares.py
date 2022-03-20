#contagem de numero de 1 a 50 mostrando somente numeros pares:

#1°: importar o sleep
from time import sleep

#2°: RANGE de (1,51) se o numero é divisivel por 2 ele é par!
#for n in range(1, 51):
 #   if n % 2 == 0:
   #     print(n, end=" ")
    #    sleep(0.4)
#print("---!!!FIM!!---")

#3°: Laço de repetição iniciando no número 2, até 51, pulando de 2 em 2.
for n in range(2, 51, 2):
    print('.', end=' ')
    print(n, end=" ")
print('ACABOU')


