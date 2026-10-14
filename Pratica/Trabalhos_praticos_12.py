#Exercicio 1
def k(x):
    if x >= 100:
        return 20

    elif x >= 50:
        return 10

    else:
        return 0




print(k(((1664525 * 145 + 1013904223) % 2**32) % 150))
print(k(((1664525 * 135 + 1013904223) % 2**32) % 150))
print(k(((1664525 * 18 + 1013904223) % 2**32) % 150))
print(k(((1664525 * 26 + 1013904223) % 2**32) % 150))
print(k(((1664525 * 127 + 1013904223) % 2**32) % 150))



#Exercicio 2
def c(b):
    if b < 10:
        return b + 19

    elif 10 <= b < 34:
        return b * 5

    elif 34 <= b < 61:
        return b // 4

    elif 61 <= b < 84:
        return b % 7

    elif b >= 84:
        return b ** 2



print(c(61) + c(32) + c(86))
print(c(84) + c(7) + c(52))
print(c(34) + c(-6) + c(77))
print(c(10) + c(44) + c(96))
print(c(10) + c(61) + c(82))