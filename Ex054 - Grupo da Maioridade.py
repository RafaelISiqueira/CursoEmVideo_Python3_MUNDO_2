#Ler o ano de nascimento de 7 pessoas, mostrar quantas já atingiram a +18 e quantas não:
from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nascimento = int(input("Em que ano a {}° pessoa nasceu? ".format(pessoa)))
    idade = atual - nascimento
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print("\nAo todo tivemos {} pessoas maiores de idade!!!".format(totalmaior))
print("\nE tambem tivemos {} pessoas menores de idade!!!".format(totalmenor))