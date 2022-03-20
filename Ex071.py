#Simulador de Caixa Eletronico:

#1°: Um pouco de firula para deixar bonito
print('='*30)
print('{:^30}'.format('BANCO DO RAFA'))
print('='*30)

#2: definir O valor necessario e as susa cédulas.
valor = int(input("Digite o Valor que você quer sacar? R$ "))
total = valor
cedula = 50
totalcedulas = 0

#3°: Criar um While True para definir o calcula a ser feito
while True:
    if total >= cedula:
        total -= cedula
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f"total de {totalcedulas} Cédulas de R${cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedulas = 0
        if total == 0:
            break
print('='*30)
print('\n!!!Volte sempre!!!')
