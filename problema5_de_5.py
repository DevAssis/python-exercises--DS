from impressao import imprime

valido = False

while valido == False:
    int1 = int(input('Informe o primeiro valor: '))
    int2 = int(input('Informe o segundo valor: '))
    if int2 <= int1:
        print('Valor invalido. Tente de novo')
    else:
        valido = True

imprime(int1, int2)




