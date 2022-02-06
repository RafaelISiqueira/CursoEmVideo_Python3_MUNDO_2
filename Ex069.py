#Pedir Idade e sexo dos cadastrados, e mostrar:
#1°: Pessoas maiores de 18 anos;
#2°: Total de homens cadastrados;
#3°: Mulheres com menos de 20 Anos.

total18 = totalH = totalM20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalH += 1
    if sexo ==  'F' and idade < 20:
        totalM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer Continuar? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Ao todo temos {totalH} HOMENS cadastrados')
print(f' E temos {totalM20} MULHERES com menos de 20 anos')

