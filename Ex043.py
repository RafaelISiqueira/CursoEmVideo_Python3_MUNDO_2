# Ler peso e altura, calcular o IMC e mostrar:
# Abaixo de 18.5 == Abaixo do peso
# Entre 18.5 e 25 == Peso Ideal
# 25 até 30 == Sobrepeso
# Acima de 40: Obesidade mórbida

#1°: Aréa para digitar peso e altura:
peso = float(input("Digite aqui o seu PESO (Kg): "))
altura = float(input("Digite aqui a sua ALTURA: "))

#2: Calculo para o IMC (peso sobre altura ao quadrado)
IMC = peso / (altura ** 2)
print("O seu indice de massa corportal é de {:.1f}".format(IMC))

#3: IF e Elif para classificação do IMC:
if IMC < 18.5:
    print("Você esta ABAIXO DO PESO ideal, PROCURE um NUTRICIONISTA")
elif 18.5 <= IMC < 25.0:
    print("Parabéns, Você esta no seu peso IDEAL")
elif 25.0 <= IMC < 30:
    print("Você esta SOBREPESO, PROCURE um NUTRICIONISTA")
elif 30. <= IMC < 40.0:
    print("Você esta com OBESIDADE, CUIDADO, Procure um NUTRICIONISTA")
elif IMC >= 40:
    print("CUIDADO, VOcê esta com OBESIDADE MÓRBIDA, Procure um profissional de saúde com !!!URGENCIA!!!")


