from regressao import *

quantidade = int(input('Informe a quantidade de variáveis do modelo: '))
x_ = list(range(0, quantidade))
y_ = list(range(0, quantidade))

print('Entrada de variáveis dependentes')
for n in range(0, quantidade):
    y_[n] = int(input(f'Informe a {n + 1}ª variável dependente: '))

print('Entrada de variáveis independentes')
for n in range(0, quantidade):
    x_[n] = int(input(f'Informe a {n + 1}ª variável independente: '))

prever = float(input(f'Informe a variável que quer prever: '))

cor = correlacao(x_, y_)
incl = inclinacao(x_, y_, cor)
inter = interceptacao(x_, y_, incl)
result = previsao(inter, incl, prever)

print('Modelo:')
print('Correlação: ', cor)
print('Inclinação: ', incl)
print(' Interceptação: ', inter)
print('Valor para prever: ', prever)
print('Resultado da previsão: ', result)