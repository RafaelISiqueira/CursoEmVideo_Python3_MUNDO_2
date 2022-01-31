#Leia um numero inteiro qualquer e escolher a base de conversão, binario, octal ou hexadecimal.

#1°: Valor do número inteiro:
num = int(input("Digite, Um número inteiro: "))

#2°: Print das opções para conversão:
print('''Escolha uma das bases para conversão:
    [ 1 ] Converter para BINÁRIO
    [ 2 ] Converter para OCTAL
    [ 3 ] Converter para HEXADECIMAL''')
#3°: Digitar uma das opções acima
opção = int(input('Digite, Sua opção de conversão: '))

#4°: If, Elif e Else !!!NÃO ESQUECER DOS .FORMAT e de tirar os 2 primeiros digitos!!!
if opção == 1:
    print("O número {}, Convertido para BÍNARIO, é igual a {}".format(num, bin(num)[2:]))
elif opção == 2:
    print("O número {}, Convertido para Octal, é igual a {}".format(num, oct(num)[2:]))
elif opção == 3:
    print("O numero {}, Convertido para HEXADECIMAL, é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção INVÁLIDA. Tente novamente.")
