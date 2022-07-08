from datetime import date

ano_nascimento = int(input('Informe o ano de nascimento: '))
ano = date.today().year
idade = ano - ano_nascimento
if idade >= 18:
    print('Está habito a alistar')
else:
    print('Não esta habito')