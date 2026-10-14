
#Exercicio 1

from random import seed
from random import uniform
seed(8704)
s_1 = round(uniform(1.0, 9.0), 2)
s_2 = round(uniform(1.0, 9.0), 2)
s_3 = round(uniform(1.0, 9.0), 2)
s_4 = round(uniform(1.0, 9.0), 2)


pago = round((s_1 + s_2 + s_3 + s_4) / 4, 2)

print(round(s_4, 2) == 8.65)               
print(pago == 3.69)                         
print(round(pago - s_2, 2) == 0.49)         
print(round(pago - s_1, 2) == 2.41)         
print(round(s_3, 2) == 1.46)               




#Exercicio 2

from random import seed
from random import uniform

def h(a, b, c, d, e):
    return round((a + b + c + d + e) / 5, 2)


n = h(1.0, 2.0, 3.0, 4.0, 5.0)
print(n)
seed(6025)
w_1 = round(uniform(1.0, 9.0), 2)
w_2 = round(uniform(1.0, 9.0), 2)
w_3 = round(uniform(1.0, 9.0), 2)
w_4 = round(uniform(1.0, 9.0), 2)
w_5 = round(uniform(1.0, 9.0), 2)
n = h(w_1, w_2, w_3, w_4, w_5)


print(round(n - w_2, 2) == 0.62)
print(round(w_3, 2) == 7.65)
print(round(w_4, 2) == 8.57)
print(n == 6.4)
print(round(n - w_1, 2) == 2.13)





