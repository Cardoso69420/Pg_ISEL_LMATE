#Exercicio 1
from random import seed
from random import choices
from random import randint

seed(9756)

def d_1(list):
    return list[0]

def d_2(list):
    return list[-1]

def d_3(list, start, end):
    return list[start:end]

def d_4(list, start):
    return list[start:]

def d_5(list, end):
    return list[:end]


z = [2, 8, 3, 9, 7, 0, 6, 1, 5, 4]

print(d_1(z))
print(d_2(z))
print(d_3(z, 2, 7))
print(d_4(z, 4))
print(d_5(z, 5))

z_1 = choices(range(10000), k=randint(4000, 5000))
z_2 = choices(range(10000), k=randint(4000, 5000))
z_3 = choices(range(10000), k=randint(4000, 5000))
z_4 = choices(range(10000), k=randint(4000, 5000))
z_5 = choices(range(10000), k=randint(4000, 5000))


print(sum(d_3(z_5, 194, 4143)))
print(d_2(d_3(z_2, 119, 4016)))
print(d_1(d_3(z_1, 180, 4758)))
print(d_1(d_4(z_3, 159)))
print(d_2(d_5(z_4, 4760)))
