l = int(0)
c = int(0)
tab = []

while (l <= 0 or l >= 10000):
    l = int(input("Qual será a largura? ")) # X

while (c <= 0 or c >= 10000):
    c = int(input("Qual será o comprimento? ")) # Y

def criarMatriz(l, c):
    for i in range(c):
        tab.append([0]*l)
    return tab

def verificarMatriz(l, c):
    criarMatriz(l, c)
    first = 0
    quantidade = 0
    for i in range(c):
        first = 1
        if (i % 2 == 0):
            for j in range(l):
                if (first == 1):
                    first = 0
                    tab[i][j] = 1
                    quantidade += 1
                elif tab[i][j - 1] == 0:
                    tab[i][j] = 1
                    quantidade += 1
    return quantidade

print(verificarMatriz(l, c))