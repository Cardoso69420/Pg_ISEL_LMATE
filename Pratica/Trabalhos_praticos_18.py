from random import seed
from random import choice
from random import randint

seed(9090)

def d(relatorio, tipo, limite):
    contador = 0
    registos = relatorio.split(';')
    for r in registos:
        partes = r.split(':')
        codigo = partes[0].strip().upper()
        abertura = float(partes[1].strip().replace(',', '.'))
        if codigo[0:3] == tipo and abertura > limite:
            contador = contador + 1
    return contador

e = 'PIL-01: 0,30; vig-02:0,45 ; pil-03:0,10;PIL-04 : 0,35;laj-01:0,50'
print(e)
g = d(e, 'PIL', 0.2)
print(g)
g = d(e, 'PIL', 0.3)
print(g)
g = d(e, 'VIG', 0.2)
print(g)

codes = ['PIL', 'pil', 'Pil', 'VIG', 'vig', 'LAJ', 'laj']
spaces = ['', ' ']

def random_item():
    code = choice(codes) + '-' + str(randint(10, 99))
    number = '0,' + str(randint(10, 99))
    return choice(spaces) + code + choice(spaces) + ':' + choice(spaces) + number + choice(spaces)

s_1 = []
s_2 = []
s_3 = []
s_4 = []
s_5 = []

for n in range(1000):
    s_1.append(random_item())
    s_2.append(random_item())
    s_3.append(random_item())
    s_4.append(random_item())
    s_5.append(random_item())

e_1 = ';'.join(s_1)
e_2 = ';'.join(s_2)
e_3 = ';'.join(s_3)
e_4 = ';'.join(s_4)
e_5 = ';'.join(s_5)

print('só para verificação dos valores pseudoaleatórios gerados')
print(s_5[0])
print(s_5[1])
print(s_5[998])
print(s_5[999])

# Respostas
print('1.1', d(e_2, 'VIG', 0.3), '-> afirmação: 61')
print('1.2', d(e_1, 'PIL', 0.2), '-> afirmação: 402')
print('1.3', d(e_3, 'LAJ', 0.4), '-> afirmação: 161')
print('1.4', d(e_4, 'PIL', 0.5), '-> afirmação: 41')
print('1.5', d(e_5, 'VIG', 0.6), '-> afirmação: 130')
