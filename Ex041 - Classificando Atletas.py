#Ler o ano de Nascimento de um atleta de natação e mostrar sua catégoria:
# <= 9 == MIRIM
# <= 14 ==INFANTIL
# <= 19 == JUNIOR
# <= 25 == SÊNIOR
# >25 == MASTER

#1°: Importar date:
from datetime import date
atualmente = date.today().year

#2°: Digitar o nascimento:
nascimento = int(input("Digite o Ano de Nascimento do Atleta: "))

#3°: Calculo da Idade
idade = atualmente - nascimento
print("O atleta tem {} anos de idade.".format(idade))

#4: IF, ELIF e ELSE, !!!TABELA DE CLASSIFICAÇÃO!!!
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JUNIOR")
elif idade <= 25:
    print("Classificação: SENIOR")
else:
    print("Classificação: MASTER")
