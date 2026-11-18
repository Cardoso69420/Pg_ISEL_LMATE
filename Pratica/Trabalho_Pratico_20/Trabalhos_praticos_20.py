#Exercicio 1
from random import seed
from random import choice
from random import randint

seed(4164)

def r(file_name):
    codes_list = []
    with open(file_name) as file:
        for line in file:
            codes_list.append(line.strip('\n'))
    return codes_list



with open('codes.txt', 'w', encoding='utf8') as file:
    file.write('BEB-412\n')
    file.write('MER-1187\n')
    file.write('LIM-33\n')
    
a = r('codes.txt')

categories = ['BEB', 'MER', 'LIM']

def write_random_file(filename):
    with open(filename, 'w', encoding='utf8') as file:
        n_lines = randint(500, 1000)
        for n in range(n_lines):
            number = randint(1, choice([9, 99, 999, 9999]))
            code = choice(categories) + '-' + str(number)
            file.write(code + '\n')
    return code

write_random_file('g_1.txt')
write_random_file('g_2.txt')
write_random_file('g_3.txt')
write_random_file('g_4.txt')
aux = write_random_file('g_5.txt')


print(len(r('g_5.txt')[-1]))
print(str(r('g_3.txt')).count('MER'))
print(r('g_2.txt')[122 - 1])
print(len(r('g_1.txt')))
print(r('g_4.txt')[0])