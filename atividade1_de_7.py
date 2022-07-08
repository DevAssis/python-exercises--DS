
tamanho = int(input('Qual tamanho da lista: '))

lista = list(range(0, tamanho))

for n in range(0, tamanho):
    lista[n] = input(f'Entre com o {n+1}º nome: ')

for n in range(0, tamanho):
    print(lista[n].capitalize())