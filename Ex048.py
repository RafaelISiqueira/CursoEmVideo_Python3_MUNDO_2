# Soma de todos os números, que são multiplos de 3 no intervaldo de ( 1 , 500)

#1°: Atribuir soma e contador:
soma = 0
contador = 0

#2°: Contar todos os numeros de 1 há 500 e dividilos por 3:
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c # Reduzi soma = soma + C
        contador += 1 # Rezuzi Contados = contador + C
#3°: Printar o resultado:
print("A soma de todos os {} valores solicitados é {}".format(contador, soma))
