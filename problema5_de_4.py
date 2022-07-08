# soma = 0
# contador = 0
# quantidade = int(input('Quantos numeros vai entrar: '))
# while contador < quantidade:
#         contador = contador + 1
#         numero = int(input('Entre com numero: '))
#         soma = soma + numero
# media = soma/quantidade
# print('A media é: ', media)

quantidade = int(input('Quantos numeros vai entrar: '))
soma = 0
for quantidade in range(1,quantidade + 1):
        numero = int(input(f'Entre com o {quantidade}º numero: '))
        soma = soma + numero
print('A media é: ', soma/quantidade)

