META = 23

def imprime(mat):
    for x in mat:
        print(x)
    print()

def puntos_casilla(lab, f, c):
    # Los 1 no suman puntos; solo los 3 y 4
    if lab[f][c] > 1:
        return lab[f][c]
    return 0

def valido(lab, res, f, c, puntos):
    # Que no salga de los bordes
    if f < 0 or f >= len(lab):
        return False
    if c < 0 or c >= len(lab[0]):
        return False
    # Que no se haya recorrido
    if res[f][c] == 1:
        return False
    # Que no sea una pared
    if lab[f][c] == 0:
        return False
    # Solo se puede entrar a F en caso de que se llega a la meta
    if f == 0 and c == 0:
        if puntos + puntos_casilla(lab, f, c) < META:
            return False
    return True


def laberB(lab, res, f, c, puntos):
    if f == 0 and c == 0:  # caso base: El ratón llegó a la salida
        if valido(lab, res, f, c, puntos):
            res[f][c] = 1
            imprime(res)
            return True
        else:
            return False
    else:
        if valido(lab, res, f, c, puntos):
            res[f][c] = 1
            puntos += puntos_casilla(lab, f, c)
            if laberB(lab, res, f-1, c, puntos):      # arriba
                return True
            elif laberB(lab, res, f, c+1, puntos):    # derecha
                return True
            elif laberB(lab, res, f+1, c, puntos):    # abajo
                return True
            elif laberB(lab, res, f, c-1, puntos):    # izquierda
                return True
            else:
                res[f][c] = 0
                imprime(res)                          # backtracking
            return False
        else:
            return False


def total_puntos(lab, res):
    total = 0
    for f in range(len(lab)):
        for c in range(len(lab[0])):
            if res[f][c] == 1:
                total += puntos_casilla(lab, f, c)
    return total

#F[0][0] = 1 e I[8][0] = 1
lab = [
    [1, 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    [1, 1, 3, 1, 0, 1, 1, 1, 1],
]

res = [[0 for _ in range(9)] for _ in range(9)]

print()
print("Laberinto original:")
print()
imprime(lab)

filas = len(lab)
if laberB(lab, res, filas - 1, 0, 0):
    print("¡El ratón logró salir del laberinto! Camino:")
    imprime(res)
    print("Puntos obtenidos:", total_puntos(lab, res))
else:
    print("El ratón NO logró salir: ningún camino suma", META, "puntos.")
    imprime(res)