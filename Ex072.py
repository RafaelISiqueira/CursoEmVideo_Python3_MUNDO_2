contador = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onde', 'dose', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', "vinte")

while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        print(f'Você digitou o número {contador[núm]}')
    elif núm > 20:
        break
    else:
        print('Números negativos invalidos, Tente Novamente. ')
print('-='*20)
print('Programa finalizado com sucesso!!!')