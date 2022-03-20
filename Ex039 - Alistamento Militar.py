#Ler o ano de nascimento:
#e ver se, Ainda vai se alistar
#se esta na Hora de se alistar
#se já Passou do tempo de se alistar
#(mostrar quanto tempo falta ou passou)

#1°: Importar date:
from datetime import date
atualmente = date.today().year

#2°: Digitar o nascimento:
nascimento = int(input("Digite aqui, O Seu Ano de Nascimento: "))

#3°: Calculo da Idade
idade = atualmente - nascimento
print("Você nasceu em {} e tem {} anos de idade em {}.".format(nascimento, idade, atualmente))

#4°: If, Elif, Else E "RESULTADO DO CALCULO DA IDADE"
if idade == 18:
    print("Esta em tempo de se alistar, Procure a JUNTA DE SERVIÇO MILITAR mais proxima!")
elif idade < 18:
    result = 18 - idade
    print("Ainda faltam {} anos para o seu alistamento militar".format(result))
    ano = atualmente + result
    print("Seu alistamento militar, será em {}".format(ano))
elif idade > 18:
    result = idade - 18
    print("Você já se alistou, ou deveria ter se alistado há {} anos.".format(result))
    ano = atualmente - result
    print("Seu alistamento foi em {}!".format(ano))

