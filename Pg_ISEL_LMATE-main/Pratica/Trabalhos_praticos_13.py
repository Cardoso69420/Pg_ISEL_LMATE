from random import seed
from random import choices
from random import randint

seed(4128)

g = [73, 12, 50, 49, 88, 5, 61, 30]

def r(list):
    count = 0

    for i in range(len(list)):
        if list[i] >= 50:
            count += 1  
    return count


z = r(g)


print(g)
print(z)

g_1 = choices(range(0, 101), k=randint(10000, 10999))
g_2 = choices(range(0, 101), k=randint(11000, 11999))
g_3 = choices(range(0, 101), k=randint(12000, 12999))
g_4 = choices(range(0, 101), k=randint(13000, 13999))
g_5 = choices(range(0, 101), k=randint(14000, 14999))

print(r(g_1))
print(r(g_4))
print(r(g_3))
print(r(g_5))
print(r(g_2))
