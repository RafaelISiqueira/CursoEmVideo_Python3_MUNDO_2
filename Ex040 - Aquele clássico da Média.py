#Calcular a média de um aluno e mostrar:
# < 5 == REPROVADO
# > 5,0 e < 6,9 == RECUPERAÇÂO
# => 7 APROVADO

#1°: Digitar o Valor das Notas:
P1 = float(input("Digite a nota da PRIMEIRA prova: "))
P2 = float(input("Digite a nota da SEGUNDA prova: "))

#2°: Calculo da média:
média = (P1 + P2) / 2
print("Tirando {:.1f} na PRIMEIRA PROVA e {:.1f} na SEGUNDA PROVA, a média do aluno é {:.1f}".format(P1, P2, média))

#3°: If, Elif
if 7 > média >= 5:
    print("O aluno está em RECUPERAÇÂO!!!")
elif média < 5:
    print("O Aluno está REPROVADO!!!")
elif média >= 7:
    print("O Aluno está APROVADO.")
