from random import seed
from random import choices
from random import randint

seed(6126)

r = [73, 12, 50, 49, 88, 5, 61, 30]
m = [55, 90, 50, 80, 64, 70, 49, 51]

def u(list_a, list_b):
    count = 0
    for i in range(len(list_a)):
        if list_a[i] >= 50 and list_b[i] >= 50:
            count += 1
    return count

b = u(r, m)

print(r)
print(m)
print(b)
r_1 = choices(range(0, 101), k=randint(10000, 10999))
m_1 = choices(range(0, 101), k=len(r_1))
r_2 = choices(range(0, 101), k=randint(11000, 11999))
m_2 = choices(range(0, 101), k=len(r_2))
r_3 = choices(range(0, 101), k=randint(12000, 12999))
m_3 = choices(range(0, 101), k=len(r_3))
r_4 = choices(range(0, 101), k=randint(13000, 13999))
m_4 = choices(range(0, 101), k=len(r_4))
r_5 = choices(range(0, 101), k=randint(14000, 14999))
m_5 = choices(range(0, 101), k=len(r_5))


print(u(r_3, m_3))
print(u(r_1, m_1))
print(u(r_2, m_2))
print(u(r_5, m_5))
print(u(r_4, m_4))
