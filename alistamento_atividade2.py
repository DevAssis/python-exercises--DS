from datetime import date

ano_nascimento = int(input('Informe o ano de nascimento: '))
ano = date.today().year
idade = ano - ano_nascimento
if idade >= 18:
    print('Está hábito a alistar')
else:
    print('Não esta hábito')