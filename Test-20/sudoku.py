"""

Este algoritmo resuelve el problema sudoku con la tecnica BakcTracking.

Ejemplo de entrada:

5 3 0  0 7 0  0 0 0  
6 0 0  1 9 5  0 0 0
0 9 8  0 0 0  0 6 0

8 0 0  0 6 0  0 0 3
4 0 0  8 0 3  0 0 1
7 0 0  0 2 0  0 0 6

0 6 0  0 0 0  2 8 0
0 0 0  4 1 9  0 0 5
0 0 0  0 8 0  0 7 9

===================

Salida:

0: 5 3 4  6 7 8  9 1 2
1: 6 7 2  1 9 5  3 4 8
2: 1 9 8  3 4 2  5 6 7

3: 8 5 9  7 6 1  4 2 3
4: 4 2 6  8 5 3  7 9 1
5: 7 1 3  9 2 4  8 5 6

6: 9 6 1  5 3 7  2 8 4
7: 2 8 7  4 1 9  6 3 5
8: 3 4 5  2 8 6  1 7 9

"""

# dimension del board
N = 9

"""
Funcion para imprimir el board
@param board
@param N
"""
def print_board(board, N):
    for i in range(N):
        for k in range(N):
            print(board[i][k], end=' ')
        print()
    print("=" * (N * 2 - 1))

"""
Funcion para obtener las coordenadas iniciales de un index en el board.
(i.e. Si el index es 0, entonces esta en el primer subboard del board)
@param index : indice actual
@return x, y : coordenadas en el board
"""
def get_limits(index):
    x, y = 0, 0
    if index >= 0 and index <= 2: x, y = 0, 2
    elif index >= 3 and index <= 5: x, y = 3, 5
    elif index >= 6 and index <= 8: x, y = 6, 8
    return x, y

"""
Funcion para verificar si se puede colocar un valor ("value") en la position (i,k)
@param board : tablero
@parsm i : fila
@param k : columna
@param value : valor
@return bool : True si se puede asignar el valor en la position (i,k), False de lo contrario.
"""
def check_put(board, i, k, value):
    
    # check subboard 
    start_row, end_row, = get_limits(i)
    start_column, end_column, = get_limits(k)

    for row in range(start_row, end_row + 1):
        for column in range(start_column, end_column + 1):
            if board[row][column] == value: 
                return False
    # check top
    
    for offset in range(0, N):
        new_i = i + -offset
        if new_i >= 0 and board[new_i][k] == value:
            return False

    # check bottom
    for offset in range(0, N):
        new_i = i + offset
        if new_i < N and board[new_i][k] == value:
            return False
    # check left

    for offset in range(0, N):
        new_k = k + -offset
        if new_k >= 0 and board[i][new_k] == value:
            return False
    # check right
    for offset in range(0, N):
        new_k = k + offset
        if new_k < N and board[i][new_k] == value:
            return False
    return True

"""
Funcion para resolver el sudoku usando backtracking
@param board : tablero
@param curr_row : fila actual
@param curr_col : columna actual
"""
def solve(board, curr_row, curr_col):

    # verifica si se ha llegado al final
    if curr_row == N - 1 and curr_col == N:
        print_board(board, N)
        return
    
    # si la columna actual es igual a N, entonces pasa a la siguiente fila
    elif curr_col == N:
        curr_row += 1
        curr_col = 0
    
    # si el valor actual en (curr_row, curr_col) es 0, entonces se busca una valor valido
    if board[curr_row][curr_col] == 0:
        for val in range(1, 9 + 1):
            # verifica si se puede asignar el valor
            if check_put(board, curr_row, curr_col, val):   
                board[curr_row][curr_col] = val
                solve(board, curr_row, curr_col + 1)
                board[curr_row][curr_col] = 0
    else:
        solve(board, curr_row, curr_col + 1)

"""
Funcion principal
@param arg: argumentos
"""
def main(arg):
    board = [list(map(int, row.split())) for row in arg]
    solve(board, 0, 0)

if __name__ == "__main__":

    board = ["5 3 0 0 7 0 0 0 0", 
             "6 0 0 1 9 5 0 0 0", 
             "0 9 8 0 0 0 0 6 0", 
             "8 0 0 0 6 0 0 0 3", 
             "4 0 0 8 0 3 0 0 1", 
             "7 0 0 0 2 0 0 0 6", 
             "0 6 0 0 0 0 2 8 0", 
             "0 0 0 4 1 9 0 0 5", 
             "0 0 0 0 8 0 0 7 9"]
    main(board)


