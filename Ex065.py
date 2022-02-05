#Crie um programa que leia um numero, até pedir para parar, e que mostre a média e seu maior valor:
resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma / quant
print('Você degitou ({}) números e a média foi ({})'.format(quant, media))
print('O maior valor foi de ({}) e o menor foi ({})'.format(maior, menor))
