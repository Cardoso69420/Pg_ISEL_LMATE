#Exercicio 1

from random import seed
from random import choice

seed(4873)

def n(j, c):
    return (not j) or c


def d(j, c):
    return n(j, c) and n(c, j)


def u(j, c, i):
    return n((d(i ,c)) , (j and j)) or n(j, c)


print("1.1", u(False, False, False))
print("1.2", u(True, True, False))
print("1.3", u(False, False, True))
print("1.4", u(False, True, False))
print("1.5", u(True, True, True))



#Exercicio 2

from random import seed
from random import choice

seed(8432)


def p(k, z, u):
    return ((z and u) and (k and k) and (k or u))



print("2.1", p(True, True, False))
print("2.2", p(False, False, False))
print("2.3", p(True, False, True))
print("2.4", p(True, False, False))
print("2.5", p(False, True, False))

