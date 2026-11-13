from random import seed
from random import choice
from random import randint

seed(9934)

def m(price_table, category, minimum_price):
    count = 0
    for regist in price_table.split(';'):
        code, price = regist.split(':')
        price = float(price.replace(',', '.'))
        if code.startswith(category) and price > minimun_price:          
            count += 1
    return count

y = 'BEB-01:1,50;MER-02:2,49;BEB-03:0,79;BEB-04:3,20;LIM-01:4,10'
print(y)
b = m(y, 'BEB', 1.0)
print(b)
b = m(y, 'BEB', 1.5)
print(b)
b = m(y, 'MER', 1.0)
print(b)

codes = ['BEB', 'MER', 'LIM']

def random_item():
    code = choice(codes) + '-' + str(randint(10, 99))
    number = str(randint(0, 9)) + ',' + str(randint(1, 9)) + '0'
    return code + ':' + number

j_1 = []
j_2 = []
j_3 = []
j_4 = []
j_5 = []

for n in range(1000):
    j_1.append(random_item())
    j_2.append(random_item())
    j_3.append(random_item())
    j_4.append(random_item())
    j_5.append(random_item())

y_1 = ';'.join(j_1)
y_2 = ';'.join(j_2)
y_3 = ';'.join(j_3)
y_4 = ';'.join(j_4)
y_5 = ';'.join(j_5)

print('só para verificação dos valores pseudoaleatórios gerados')
print(j_5[0])
print(j_5[1])
print(j_5[998])
print(j_5[999])

# Respostas
print(m(y_2, 'MER', 2.5))
print(m(y_5, 'MER', 5.5))
print(m(y_1, 'BEB', 1.5))
print(m(y_4, 'BEB', 4.5))
print(m(y_3, 'LIM', 3.5))
