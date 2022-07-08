quantidade = False

while quantidade == False:
    qtda = int(input('Quantos numeros irá usar?(Maior ou igual a 2: '))
    if qtda >= 2:
        quantidade = True
    else:
        print('Quantidade invalida. Tente novamente.')

lista = list(range(0,qtda))

for n in range(0,qtda):
    lista[n] = int(input(f'Entre com o {n+1}º numero:'))

soma = lista[0] + lista[qtda-1]
produto = lista[0] * lista[1]

print('A soma do primeiro com o ultimo da lista é: ', soma)
print('O produto do primeiro com o segunda da lista é:', produto)
