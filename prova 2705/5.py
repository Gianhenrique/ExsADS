matriz = []

def criarMatriz():
    for i in range(43):
        matriz.append([0]*3)
    return matriz

def criarPonderacao():
    for i in matriz:
        for j in matriz:
