#Exercicio 1
from random import randint
from random import seed
from random import randint


def t(e):
    return 2*e**3 + 3*e**2 + 5*e + 4


seed(1500)

e_1 = randint(1, 1000)
e_2 = randint(1, 1000)
e_3 = randint(1, 1000)
e_4 = randint(1, 1000)
e_5 = randint(1, 1000)

p = t(e_1)

print(p)




#Exercicio 2
from random import seed
from random import randint

def u(h, e):
    return 9*(h - e)**3 + 6*(h + e)**2 + 3*h*e + 4

seed(2366)

h_1 = randint(1, 1059)
h_2 = randint(1, 1059)
h_3 = randint(1, 1059)
h_4 = randint(1, 1059)
h_5 = randint(1, 1059)
e_1 = randint(1, 1059)
e_2 = randint(1, 1059)
e_3 = randint(1, 1059)
e_4 = randint(1, 1059)
e_5 = randint(1, 1059)


m = u(h_2, e_2)

print(m)