#Criar uma progressão aritimética usando o WHILE:

primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} =---> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
