from random import seed
from random import randint
from random import choices

seed(5656)

def u(tabela, cliente):
    contador = 0
    for valor in tabela[cliente - 1]:
        if valor != 0:
            contador += 1
    return contador

def w(tabela, cliente):
    total = 0
    for valor in tabela[cliente - 1]:
        total += valor
    return total

s = [
    [2, 0, 1, 0],
    [0, 0, 5, 0],
    [1, 3, 0, 4]
]
print(u(s, 1))
print(w(s, 1))
print(u(s, 3))
print(w(s, 3))

number_of_clients = randint(500, 600)
number_of_products = randint(500, 600)
g_1 = []
for y in range(number_of_clients):
    g_1.append(choices([0, 0, 0, 0, 0, 1, 2, 3, 4, 5], k=number_of_products))

print('só para verificação dos valores pseudoaleatórios gerados')
print(g_1[0][0])
print(g_1[0][-1])
print(g_1[-1][0])
print(g_1[-1][-1])

print(u(g_1, 428))                
print(number_of_products)          
print(w(g_1, 498))                
print(number_of_clients)          
print(w(g_1, 544))                