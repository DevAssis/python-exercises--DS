validado = True
def conversor(tipo, valor):
    if tipo.upper() == 'C':
        c = (valor - 32) / 1.8
        print(f'Temperatura em Celsus é: {c:.2f}º Celsus')
    else:
        f = (valor * 1.8) + 32
        print(f'Temperatura em Fahrenheit é: {f:.2f}º F')


while validado == True:
    tipo = input('''Entre com o tipo de Conversão.
Para Celsus(C) ou para fahrenheit(F) - C/F: ''')
    if tipo.upper() == 'C' or tipo.upper() == 'F':
        validado = False
    else:
        print('Entre com F ou C: ')


valor = float(input('Entre com a temperatura: '))

conversor(tipo, valor)






