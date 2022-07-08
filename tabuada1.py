p = 'S'
while p == 'S':

    def tabu():
        for s in range(1, 11):
            print(f'{n} x {s:2} = ', n * s)
        print('-' * 15)
        print(f'Fim da Tabuada do {n}')

    n = int(input('Entre com o numero da tabuada: '))
    tabu()
    p = input('Calcular outra Tabuada?(S/N):')
    p = p.upper()

print('Obrigado. Até mais')








