from random import seed
from random import randint
from random import choices

seed(5656)

def u(table, client_number):
    count = 0
    for i in range(len(table[client_number - 1])):
        if table[client_number - 1][i] != 0:
            count += 1
    return count

def w(table, client_number):
    sum = 0
    for i in range(len(table[client_number - 1])):
        sum += table[client_number - 1][i]
    return sum

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
