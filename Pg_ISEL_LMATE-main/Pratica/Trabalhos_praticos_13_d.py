from random import seed
from random import choices

seed(8799)

q = [3, 4, 5, 4, 7, 9, 4]

def f(n, lista):
    contador = 0
    for i in range(len(lista)):
        if lista[i] == n:
            contador += 1
    return contador


j_1 = f(5, q)
j_2 = f(4, q)
j_3 = f(2, q)

print(j_1)
print(j_2)
print(j_3)

h_1 = choices(range(100), k=1000)
h_2 = choices(range(100), k=1000)
h_3 = choices(range(100), k=1000)
h_4 = choices(range(100), k=1000)
h_5 = choices(range(100), k=1000)


    
print(f(100, h_5))
print(f(3, h_3))
print(f(78, h_4))
print(f(42, h_2))
print(f(90, h_1))