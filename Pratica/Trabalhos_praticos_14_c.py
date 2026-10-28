#Exercicio 1


#1.1
c = [12, 7, 25, 40]
for f in range(len(c)):
    print(f)


#1.2
v = [12, 7, 25, 40]
for x in range(len(v)):
    print(v[x])


#1.3
t = [12, 7, 25, 40]
for t in d:
    print(d)


#1.4
for i in [12, 7, 25, 40]:
print(i)


#1.5
a = [12, 7, 25, 40]
for a in a:
    print(a)
print(len(a))


#1.6
for e in [12, 7, 25, 40]
print(e)



#Exercicio 2

lista_de_preços = [97, 70, 15, 38, 92, 30, 86, 68, 6, 80]

# número de elementos da lista
lista_de_preços_comprimento = len(lista_de_preços)

produto = ['Farinha', 1.23, 10, True]

# número de elementos da lista
produto_comprimento = len(produto)


#2.1
n = [12, 7, 25, 40]
print(n[4])


#2.2
i = [12, 7, 25, 40]
print(i)
i.append(30)
print(i)
c = []
print(c)
c.append(30)
print(c)



#2.3
z = [12, 7, 25, 40]
print(len(z))
print(z)
print(z[len(z)])


#2.4
f = [12, 7, 25, 40]
print(f)
g = f[1]
print(g)
f[1] = 30
print(f)


#2.5
j = [12, 7, 25, 40, 18]
print(j[-1])
print(j[-2])
print(j[-4])


#2.6
x = []
print(x)


#2.7
m = ['Arroz', 0.85, 3, True]
print(m)




#Exercicio 3
from random import seed
from random import randint
from random import choices

seed(3855)

def print_matriz(matriz):
    número_linhas = len(matriz)
    número_colunas = len(matriz[0])
    print(número_linhas)
    print(número_colunas)
    for linha in matriz:
        print(linha)
    print('----------')

exemplo = [
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 11],
    [12, 13, 14, 15, 16]
]


def criar_matriz_aleatoria():
    número_linhas = randint(10, 15)
    número_colunas = randint(10, 15)
    matriz = []
    for n in range(número_linhas):
        matriz.append(choices(range(10, 100), k=número_colunas))
    return matriz


s_1 = criar_matriz_aleatoria()
s_2 = criar_matriz_aleatoria()
s_3 = criar_matriz_aleatoria()
s_4 = criar_matriz_aleatoria()
s_5 = criar_matriz_aleatoria()



# 3.1
print_matriz(s_1)
print(s_1[3])



# 3.2
print_matriz(s_4)
print(s_4[2][13])



# 3.3
print_matriz(s_3)
print(s_3[1][0])



# 3.4
print_matriz(s_5)
print(s_5[13][4])




# 3.5
print_matriz(s_2)
for linha in s_2:
    print(linha[8])


