import time

def valido(tablero, fila, columna, numero):
    # Verificar si el número ya está en la fila
    for i in range(9):
        if tablero[fila][i] == numero:
            return False

    # Verificar si el número ya está en la columna
    for i in range(9):
        if tablero[i][columna] == numero:
            return False

    # Verificar si el número ya está en el bloque 3x3
    inicio_fila = (fila // 3) * 3
    inicio_columna = (columna // 3) * 3
    for i in range(3):
        for j in range(3):
            if tablero[inicio_fila + i][inicio_columna + j] == numero:
                return False

    return True

def encontrar_celda_vacia(tablero):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                return fila, columna
    return None  # Si no hay celdas vacías, el Sudoku está resuelto

def solucion(tablero):
    # Buscar la siguiente celda vacía
    celda_vacia = encontrar_celda_vacia(tablero)
    if not celda_vacia:
        return True  # Si no hay celdas vacías, se encontro la solución

    fila, columna = celda_vacia

    # Se prueban los números del 1 al 9 en la celda vacía
    for numero in range(1, 10):
        if valido(tablero, fila, columna, numero):
            tablero[fila][columna] = numero  # Se coloca el número en la celda

            # Se intentar resolver el resto del Sudoku
            if solucion(tablero):
                return True

            # Si no se puede resolver, retroceder y probrueba el siguiente número
            tablero[fila][columna] = 0

    return False  # Si no hay solución válida, se vuelve al paso anterior

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(num) if num != 0 else '●' for num in fila))

if __name__ == "__main__":
    # Sudoku inicial
    tablero_sudoku = [
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 8, 4, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 8, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 2, 0, 9, 0],
        [9, 0, 7, 0, 0, 0, 5, 0, 0],
        [0, 0, 2, 3, 6, 0, 4, 0, 0],
        [0, 0, 3, 0, 7, 0, 0, 5, 0],
        [0, 9, 0, 5, 0, 6, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0]
    ]

    print("Tablero de Sudoku antes de resolver:")
    imprimir_tablero(tablero_sudoku)

    # Tiempo de ejecución
    tiempo_inicio = time.time()
    if solucion(tablero_sudoku):
        print("\nTablero de Sudoku después de resolver:")
        imprimir_tablero(tablero_sudoku)
    else:
        print("\nNo existe solución para el Sudoku dado.")

    tiempo_fin = time.time()
    print(f"\nTiempo de ejecución: {tiempo_fin - tiempo_inicio:.6f} segundos")
