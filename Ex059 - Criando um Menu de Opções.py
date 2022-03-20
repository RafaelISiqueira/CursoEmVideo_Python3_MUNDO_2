#Menu de opções de uma calculadora:

n1 = int(input("Digite aqui o seu PRIMEIRO valor: "))
n2 = int(input("Digite aqui o seu SEGUNDO valor: "))
opção = 0

while opção != 5:
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] DIVIDIR
    [ 4 ] MAIOR
    [ 5 ] NOVOS NÚMEROS
    [ 6 ] SAIR DO PROGRAMA''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, soma))
    elif opção == 3:
        dividir = n1 / n2
        print('A divisão entre {} / {} é {}'.format(n1, n2, dividir))
    elif opção == 4:
        if n1 > n2:
            maior = n1
        else:
            meior = n2
        print('Entre {} e {} o maior número é {}'.format(n1, n2, maior))
    elif opção == 5:
        print('Digite os números novamente: ')
        n1 = int(input("Digite aqui o seu PRIMEIRO valor: "))
        n2 = int(input("Digite aqui o seu SEGUNDO valor: "))
    elif opção == 6:
        print("FINALIZANDO PROGRAMA...")
    else:
        print('Opção inválida, Tente novamente')
    print('=-=' * 10)
print('Fim do programa! volte sempre :) ')
