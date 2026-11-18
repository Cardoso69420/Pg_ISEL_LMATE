#Exercicio 1
from random import seed
from random import choices
from random import randint

seed(2053)

def i(file_name):
    lines = []
    with open(file_name) as file:
        for line in file:
            lines.append(line)
    return lines




file = open('text.txt', 'w', encoding='utf8')
file.write('abcd\n')
file.write('efg\n')
file.write('hijkl\n')
file.close()


def write_random_file(filename):
    file = open(filename, 'w', encoding='utf8')
    n_lines = randint(500, 1000)
    for x in range(n_lines):
        n_letters = randint(500, 1000)
        random_string = ''.join(choices('abcdefghij', k=n_letters)) + '\n'
        file.write(random_string)
    file.close()
    return random_string


write_random_file('d_1.txt')
write_random_file('d_2.txt')
write_random_file('d_3.txt')
write_random_file('d_4.txt')
aux = write_random_file('d_5.txt')


print(len(i('d_2.txt')[379 - 1]))
print(i('d_5.txt')[112 - 1][291 - 1])
print(len(i('d_1.txt')))
print(i('d_3.txt')[311 - 1][430 - 1])
print(i('d_4.txt')[-1][0])

