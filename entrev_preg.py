#15/5/2023_SimonVargasRusso
#Codigo en Python
#no me parecio posible los requisitos iniciales.
# NUEVO criterio: 
# las casillas deben intercalar colores, 
# ninguna casilla puede tener otra casilla del mismo color arriba, abajo, o a sus costados.
import numpy as np

def create_chessboard(n):
    tablero = np.zeros((n, n), dtype=int)
    for i in range(n): # fila
        for j in range(n):# columna
            # Si suma de las coordenadas es par se asigna rojo
            if (i + j) % 2 == 0:
                tablero[i][j] = 1  # 1 es rojo
            else:
                tablero[i][j] = 2  # 2 es azul

    return tablero

def print_chessboard(tablero):
    n = len(tablero)
    for i in range(n):
        for j in range(n):
            if tablero[i][j] == 1:
                print("R", end=" ")  # R para el color rojo
            else:
                print("A", end=" ")  # A para el color azul
        print()

# imprimir tablero de ajedrez de 8x8, ejecutable final
t_ajedrez = create_chessboard(8)
print_chessboard(t_ajedrez)
