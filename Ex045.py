#Programa que faça jogar Jokenpô

#1°: Importar ferramenta random e time:
from random import randint
from time import sleep

#2°: Escolha do computador:
armas = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

#3°: Escolha do Jogador:
print("VAMO HO MERDA!!!")
sleep(2)
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Escolha uma das opções ACIMA: "))

#4: tempo para ''PENSAR''
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)

#5° Mostrar as escolhas do COMPUTADOR e do JOGADOR:
print('-=' * 11)
print("Eu escolhi {}".format(armas[computador]))
print("Tu escolheu {}".format(armas[jogador]))
print('-=' * 11)

#6°: If, elif e else das vitorias, derrotas e impates:
#6.1: NPC escolhe PEDRA:
if computador == 0:
    if jogador == 0:
        print('EMPATOU VAMO OUTRA, ARROMBADO!') #EMPATE
    elif jogador == 1:
        print('PORRA, PERDI ESSA MERDA!') #'JOGADOR VENCE'
    elif jogador == 2:
        print('GANHEI CARALHO, CHUPA') #'COMPUTADOR VENCE'
    else:
        print("NÃO SABE ESCOLHER OPÇÃO, BICHO BURRO, VAI DE NOVO")

#6.2:NPC escolhe PAPEL:
elif computador == 1:
    if jogador == 0:
        print('GANHEI CARALHO, CHUPA')
    elif jogador == 1:
        print('EMPATOU VAMO OUTRA, ARROMBADO!')
    elif jogador == 2:
        print('PORRA, PERDI ESSA MERDA!')
    else:
        print("NÃO SABE ESCOLHER OPÇÃO, BICHO BURRO, VAI DE NOVO")

#6.3: NPC escolhe TESOURA:
elif computador == 2:
    if jogador == 0:
        print('PORRA, PERDI ESSA MERDA!')
    elif jogador == 1:
        print('GANHEI CARALHO, CHUPA')
    elif jogador == 2:
        print('EMPATOU VAMO OUTRA, ARROMBADO!')
    else:
        print("NÃO SABE ESCOLHER OPÇÃO, BICHO BURRO, VAI DE NOVO")