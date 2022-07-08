from numpy import *

def correlacao(x, y):
    covariacao = cov(x, y, bias=True)[0][1]
    variancia_x = var(x)
    variancia_y = var(y)
    return covariacao / sqrt(variancia_x * variancia_y)

def inclinacao(x, y, correlacao):
    stdx = std(x)
    stdy = std(y)
    return correlacao * (stdy / stdx)

def interceptacao(x, y, inclinacao):
    media_y = mean(y)
    media_x = mean(x)
    return media_y - (inclinacao * media_x)

def previsao(interceptacao, inclinacao, valor):
    return interceptacao + (inclinacao * valor)
