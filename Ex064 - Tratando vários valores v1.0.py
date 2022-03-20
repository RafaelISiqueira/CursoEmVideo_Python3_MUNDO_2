# Ler varios Numeros, quando digitar 999 ele vai parar e mostrar quantos numeros foram digitados e a soma deles

num = contador = soma = 0
num = int(input("Digite um número [999 para PARAR]: "))
while num != 999:
    soma += num
    contador += 1
    num = int(input("Digite um número [999 para PARAR]: "))
print('Você digitou {} números e a soma entre eles foi de {}.'.format(contador, soma))
