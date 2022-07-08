
idade = int(input('Qual é a sua idade?: '))
escolaridade = input(f'''
Qual escolaridade:
Digite 1 -  ensino fundamental
Digite 2 -  ensino médio 
Digite 3 - ensino superior:
> '''
)
if (escolaridade == '3') or (escolaridade == 2 and idade > 60):
    print('Habilitado')
else:
    print('Não Habilitado')
    