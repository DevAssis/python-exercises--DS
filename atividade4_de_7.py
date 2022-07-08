lista = list(range(0, 5))

lista[0] = int(input('Entre com o numero na posição 1: '))
for n in range(1, 5):
    lista[n] = int(input(f'Entre com o numero na posição {n+1}: '))
    while lista[n] <= lista[n-1]:
        lista[n] = int(input(f'Numero inválido. Entre novamente com numero na posição {n+1}: '))
print(lista)