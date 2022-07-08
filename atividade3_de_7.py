
lista = list(range(0,5))

for n in range(0,5):
    lista[n] = int(input(f'Entre com o {n+1}º numero:'))

for n in range(0,5):
    numero = lista[n] ** 0.5
    print(f'Raiz quadrada do numero {lista[n]} é : {numero:.2f}')
    if numero // 1 == numero:
        print('Este numero é Inteiro')
    else:
        print('Este numero é Decimal')
