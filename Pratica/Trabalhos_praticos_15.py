#Exercicio 1
from random import seed
from random import randint
from random import choices

seed(3141)

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
print_matriz(exemplo)
print(exemplo[1])
print(exemplo[0][0])
print(exemplo[0][4])
print(exemplo[2][0])
print(exemplo[2][4])

def criar_matriz_aleatoria():
    número_linhas = randint(50, 100)
    número_colunas = randint(50, 100)
    matriz = []
    for n in range(número_linhas):
        matriz.append(choices(range(10, 100), k=número_colunas))
    return matriz

u_1 = criar_matriz_aleatoria()
u_2 = criar_matriz_aleatoria()
u_3 = criar_matriz_aleatoria()
u_4 = criar_matriz_aleatoria()
u_5 = criar_matriz_aleatoria()

print('só para verificação da geração de valores pseudoaleatórios')
print(u_1[0][0])
print(u_2[0][0])
print(u_3[0][0])
print(u_4[0][0])
print(u_5[0][0])

print(u_1[0][len(u_1[0]) - 1])    
print(u_5[47][7])                  
print(u_3[1][16])                  
print(u_4[66][60])                 
print(u_2[len(u_2) - 1][0])



#Exercicio 2
from random import seed
from random import choices
from random import randint

seed(3849)

def b(matriz, linha, coluna):
    return matriz[linha - 1][coluna - 1]

def i(matriz, linha, coluna, valor):
    matriz[linha - 1][coluna - 1] = valor

q = [
    [4, 3, 9, 12],
    [2, 6, 8, 10],
    [7, 5, 1, 11]
]

def print_matrix(q):
    for line in q:
        print(line)

print_matrix(q)
print(b(q, 1, 1))
print(b(q, 3, 4))
print(b(q, 2, 2))
i(q, 2, 4, 100)
i(q, 3, 3, 101)
i(q, 3, 4, 102)
print_matrix(q)

def get_random_matrix():
    n_lines   = randint(100, 200)
    n_columns = randint(100, 200)
    lines = []
    for x in range(n_lines):
        lines.append(choices(range(-100, 100), k=n_columns))
    for x in range(1000):
        line   = randint(1, n_lines)
        column = randint(1, n_columns)
        value  = randint(-100, 100)
        i(lines, line, column, value)
    return lines

q_1 = get_random_matrix()
q_2 = get_random_matrix()
q_3 = get_random_matrix()
q_4 = get_random_matrix()
q_5 = get_random_matrix()

print('só para verificação dos valores pseudoaleatórios gerados')
print(q_5[0][0])
print(q_5[0][1])
print(q_5[1][0])
print(q_5[1][1])

print(b(q_5, 145, 122))   
print(b(q_4, 147, 74))   
print(len(q_2[0]))       
print(len(q_1))          
print(b(q_3, 75, 188))           
