#Exercicio 1
from random import seed
from random import choices
from random import randint

seed(6212)

e = [3, 4, 4, 5, 5, 6]

def p(number, number_list):
    exists = False
    i = 0
    while exists == False and i < len(number_list):
        if number == number_list[i]:
            exists = True
        i += 1
    return exists

c_1 = p(5, e)
c_2 = p(7, e)


e_1 = choices(range(0, 10000), k=randint(5000, 5999))
e_2 = choices(range(0, 10000), k=randint(5000, 5999))
e_3 = choices(range(0, 10000), k=randint(5000, 5999))
e_4 = choices(range(0, 10000), k=randint(5000, 5999))
e_5 = choices(range(0, 10000), k=randint(5000, 5999))

print(p(3528, e_1))
print(p(4940, e_2))
print(p(4184, e_4))
print(p(1667, e_3))
print(p(4696, e_5))