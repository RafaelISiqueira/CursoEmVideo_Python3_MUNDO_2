#Tabuada V3.0, Mostrar a tabuada e o proximo valor, (númereos negativos param a calculadora):

while True:
    n = int(input("Quer ver a Tabuada de qual valor: "))
    if n < 0:
        break
    print('-='*15)
    for c in range(1,11):
        print(f"{n} x {c} = {n*c}")
    print("-="*15)
print("\nPROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!")