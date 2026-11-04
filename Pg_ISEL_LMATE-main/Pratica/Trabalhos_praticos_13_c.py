#Exercício 1
from random import seed
from random import choices

seed(5673)

y = [3, 4, 5, 4, 7, 9, 4]

def p(a, list):
    count = 0
    for i in range(len(list)):
        if list[i] == a:
            count += 1
    return count

c_1 = p(5, y)
c_2 = p(4, y)
c_3 = p(2, y)



m_1 = choices(range(100), k=1000)
m_2 = choices(range(100), k=1000)
m_3 = choices(range(100), k=1000)
m_4 = choices(range(100), k=1000)
m_5 = choices(range(100), k=1000)

print(p(90, m_3))   
print(p(2, m_1))    
print(p(99, m_2))   
print(p(106, m_5))   
print(p(70, m_4))   



#Exercicio 2
from random import seed
from random import choices
from random import randint

seed(4800)

q_1 = [2, -8, 3, 9, -7, 0, 6, 1, 5, -4]

def m(list):
    new_list = []
    negative = 0
    zeros = 0
    positive = 0

    for i in range(len(list)):
        if list[i] < 0:
            negative += 1

        elif list[i] == 0:
            zeros += 1

        else:
            positive += 1

    new_list.append(negative)
    new_list.append(zeros)
    new_list.append(positive)

    return new_list


q_1 = choices(range(-100, 100), k=randint(10000, 20000))
q_2 = choices(range(-100, 100), k=randint(10000, 20000))
q_3 = choices(range(-100, 100), k=randint(10000, 20000))
q_4 = choices(range(-100, 100), k=randint(10000, 20000))
q_5 = choices(range(-100, 100), k=randint(10000, 20000))

print(m(q_1))
print(m(q_5))
print(m(q_4))
print(m(q_2))
print(m(q_3))
