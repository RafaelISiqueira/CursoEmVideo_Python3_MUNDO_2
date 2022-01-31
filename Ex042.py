# Refazer o 035 e mostrar qual o tipo de Triangulo
# Equilátero, Isósceles ou Escaleno

#Firula
print('-=-' * 15)
print('Analisador de Triângulos')
print('-=-' * 15)

#1°: Númerar os Lados do Triangulo
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

#2: If Elif e else (usei IF dentro de IF)
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR um triângulo: ', end="")
    if n1 == n2 == n3:  #todos lados IGUAIS
        print("EQUILATERO")
    elif n1 != n2 != n3 != n1:  #todos os lados DIFERENTES
        print("ESCALENO")
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um Triângulo')