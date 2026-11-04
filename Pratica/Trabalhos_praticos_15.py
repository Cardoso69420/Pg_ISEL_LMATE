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

print(u_1[0][len(u_1[0]) - 1])    # 1.1
print(u_5[47][7])                  # 1.2
print(u_3[1][16])                  # 1.3
print(u_4[66][60])                 # 1.4
print(u_2[len(u_2) - 1][0])        # 1.5