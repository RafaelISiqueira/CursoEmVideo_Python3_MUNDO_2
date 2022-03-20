#Contagem regressiva de fogos de artificio de 10 há 0:

#1°: importar time
from time import sleep

#2: Fazer o laço de repetição?
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('KABUUUUUMMMMM')