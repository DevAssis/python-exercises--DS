repetir = True
while repetir == True:
    n = int(input('Qual tabuada: '))
    for s in range(1,11):
        print(f'{n} x {s:2} = ', n * s)
    p = input('Deseja continuar S ou N: ')
    if p.upper() == 'S':
        repetir = True
    else:
        repetir = False
