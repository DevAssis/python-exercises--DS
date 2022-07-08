cont = 0
soma = 0
produto = 1

for n in range(1,6):
    val = int(input(f'Entre com o {n}º valor: '))
    if val % 2 == 0:
        cont = cont+1
        soma = soma + val
        produto = produto * val

print('A quantidade de valores pares é : ',cont)
print('A soma dos valores pares é: ',soma)
print('O Produto dos valores é: ', produto)



