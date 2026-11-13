from random import seed
from random import choice
from random import randint

seed(9934)

def m(tabela, categoria, preco_min):
    contador = 0
    registos = tabela.split(';')
    for r in registos:
        partes = r.split(':')
        codigo = partes[0]
        preco = float(partes[1].replace(',', '.'))
        if codigo[0:3] == categoria and preco > preco_min:
            contador = contador + 1
    return contador

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
print('1.1', m(y_2, 'MER', 2.5), '-> afirmação: 767')
print('1.2', m(y_5, 'MER', 5.5), '-> afirmação: 145')
print('1.3', m(y_1, 'BEB', 1.5), '-> afirmação: 292')
print('1.4', m(y_4, 'BEB', 4.5), '-> afirmação: 185')
print('1.5', m(y_3, 'LIM', 3.5), '-> afirmação: 239')
