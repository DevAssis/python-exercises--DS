lista = list(range(0, 5))

for n in range(0, 5):
    lista[n] = int(input(f'Entre com um numero da posição {n+1}: '))
    while lista[n] <= 0:
        lista[n] = int(input('Numero invalido. Entre novamente: '))
print(lista)

for n in range(0, 5):
    if lista[n] % 2 == 0:
        print(f'numero na posição {n + 1} é par:',lista[n])

