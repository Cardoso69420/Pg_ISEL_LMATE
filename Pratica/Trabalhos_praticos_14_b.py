#Exercicio 1
from random import seed
from random import choices
from random import randint

seed(9784)

g = [2, 8, 3, 9, 7, 0, 6, 1, 5, 4]

def k(list, i):
    return list[i]



g_1 = choices(range(10000), k=randint(4000, 5000))
g_2 = choices(range(10000), k=randint(4000, 5000))
g_3 = choices(range(10000), k=randint(4000, 5000))
g_4 = choices(range(10000), k=randint(4000, 5000))
g_5 = choices(range(10000), k=randint(4000, 5000))


print(k(g_3, 1990))
print(k(g_2, 4502))
print(k(g_1, 0))
print(k(g_4, 4443))
print(k(g_5, 4090))




#Exercicio 2
from random import seed
from random import sample
from random import randint

seed(1810)

j_1 = [2, 8, 3, 9, 7, 0, 6]
j_2 = [7, 6, 4, 0, 5, 1, 9]

def x(list_a, list_b, a):
    return list_b[list_a.index(a)]


k=randint(4000, 5000)
j_1 = sample(range(10000), k)
j_2 = sample(range(10000), k)
k=randint(4000, 5000)
j_3 = sample(range(10000), k)
j_4 = sample(range(10000), k)
k=randint(4000, 5000)
j_5 = sample(range(10000), k)
j_6 = sample(range(10000), k)
k=randint(4000, 5000)
j_7 = sample(range(10000), k)
j_8 = sample(range(10000), k)
k=randint(4000, 5000)
j_9 = sample(range(10000), k)
j_10 = sample(range(10000), k)


print(x(j_9, j_10, 1577))
print(x(j_5, j_6, 1891))
print(x(j_1, j_2, 43))
print(x(j_3, j_4, 1759))
print(x(j_7, j_8, 9526))



#Exercicio 3
from random import seed
from random import choices
from random import randint
from random import sample

seed(4481)

m_1 = [2, 8, 3, 9, 7, 0, 6, 1, 5, 4]
m_2 = [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]

def q(list_a, binary_list):
    sum = 0
    for i in range(len(list_a)):
        if binary_list[i] == 1:
            sum += list_a[i]

    return sum



k=randint(4000, 5000)
m_1 = choices(range(-10000, 10000), k=k)
m_2 = choices([0, 1], k=k)
k=randint(4000, 5000)
m_3 = choices(range(-10000, 10000), k=k)
m_4 = choices([0, 1], k=k)
k=randint(4000, 5000)
m_5 = choices(range(-10000, 10000), k=k)
m_6 = choices([0, 1], k=k)
k=randint(4000, 5000)
m_7 = choices(range(-10000, 10000), k=k)
m_8 = choices([0, 1], k=k)
k=randint(4000, 5000)
m_9 = choices(range(-10000, 10000), k=k)
m_10 = choices([0, 1], k=k)


print(q(m_1, m_2))
print(q(m_7, m_8))
print(q(m_9, m_10))
print(q(m_3, m_4))
print(q(m_5, m_6))