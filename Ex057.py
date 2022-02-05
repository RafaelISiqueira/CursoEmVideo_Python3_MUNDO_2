#Criar um programa que leia o sexo (M, F), caso errado, indicar o correto:

sexo = str(input("Informe seu Sexo: [M/F] ")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))