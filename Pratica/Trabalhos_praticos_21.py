from random import seed
from random import randint

seed(8328)

def i(file_name):
    table = []
    with open(file_name, 'r') as file:
        for line in file:
            line_list = line.split(',')
            for number in line:
                line_list.append(int(number))
            table.append(line_list)
    return table

def q(table):
    sum = 0
    for line in table:
        for value in line:
            sum = sum + value
    return sum

with open('units.txt', 'w', encoding='utf8') as file:
    file.write('2,0,1,0\n')
    file.write('0,0,5,0\n')
    file.write('1,3,0,4\n')

b = i('units.txt')
print(b)
print('----------')

for line in b:
    print(line)
print('----------')
print(q(b))

def write_random_file(filename):
    with open(filename, 'w', encoding='utf8') as file:
        number_of_clients = randint(500, 1000)
        number_of_products = randint(5, 20)
        for n in range(number_of_clients):
            units = []
            for m in range(number_of_products):
                units.append(str(randint(0, 100)))
            line = ','.join(units)
            file.write(line + '\n')
    return line

write_random_file('a_1.txt')
write_random_file('a_2.txt')
write_random_file('a_3.txt')
write_random_file('a_4.txt')
aux = write_random_file('a_5.txt')

print('só para verificação dos valores pseudoaleatórios gerados')
print(aux)


print(i('a_1.txt')[458 - 1][17 - 1])
print(q(i('a_4.txt')))
print(q(i('a_2.txt')))
print(i('a_3.txt')[199 - 1][3 - 1])
print(i('a_5.txt')[416 - 1][5 - 1])
