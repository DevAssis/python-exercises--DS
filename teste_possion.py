from math import pow, factorial

def poisson(x, lam):
    return pow(2.71828, -lam) * pow(lam, x) / factorial(x)

print(poisson(3,2))
