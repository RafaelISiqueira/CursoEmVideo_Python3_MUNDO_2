#contagem de numero de 1 a 50 mostrando somente numeros pares:

#1°: importar o sleep
from time import sleep

#2°: Laço da forma ''manual''
#for n in range(1, 51):
 #   if n % 2 == 0:
   #     print(n, end=" ")
    #    sleep(0.4)
#print("---!!!FIM!!---")

#3°: Laço de repetição com ponto
for n in range(2, 51, 2):
    print('.', end=' ')
    print(n, end=" ")
print('ACABOU')


