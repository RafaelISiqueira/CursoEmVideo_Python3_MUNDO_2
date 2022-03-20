#Leia uma frase e diga se ela é um palindromo ou não:

#1°: deixa frase em Maiusculo, Sem espaços e de trás para frente:
frase = str(input('Digite uma frase aqui: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''


#2°: For para pega a primeira e a ultima letra:
#inverso = junto[::-1] (PODE SUBISTITUIR O FOR INTEIRO)(fatiamento)
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]


print("O inverso de {} é {}".format(junto, inverso))

#3°: If e else para resposta se é ou não um PALÍNDROMO:
if inverso == junto:
    print("Esta frase é um PALÍNDROMO!")
else:
    print("A Frase não é um PALÍNDROMO!")