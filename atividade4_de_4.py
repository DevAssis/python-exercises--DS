valor1 = 0
valor2 = 0
while valor1 <= 10:
    valor1 = int(input('Entre com o primeiro valor:'))
    if valor1 <= 10:
        print('Valor invalido. Tente de novo')
        continue

valor = 10 * valor1
while valor2 < valor:
    valor2 = int(input('Entre com o segundo valor:'))
    if valor2 < valor:
        print('Valor invalido. Tente de novo')
        continue
print(valor1 * valor2)
