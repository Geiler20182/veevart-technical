
"""

Entrada:
N, N e Nataules & N >= 1

Ejemplo:

4
Salida:
O O X O
X O O O
O O O X
O X O O
=======
O X O O
O O O X
X O O O
O O X O
=======

"""

import sys


global N

def print_board(board, N):
    for i in range(N):
        for k in range(N):
            print(board[i][k], end=' ')
        print()
    print("=" * (N * 2 - 1))

"""
Funcion para verificar si se puede realizar un movimiento
@param board
@param N : dimension del board
@param i : fila
@param k : columna
@return bool : True si se puede realizar un movimiento, False de lo contrario
"""
def check_move(board, N, i, k,):

    fn = lambda row, col: 1 if board[row][col] == 'X' else 0
    count_queens = 0
    for offset in range(N):
        top, bottom = -offset + i, offset + i
        left, right = -offset + k, offset + k

        if top >= 0: count_queens += fn(top, k)
        if bottom < N: count_queens += fn(bottom, k)
        if left >= 0: count_queens += fn(i, left)
        if right < N: count_queens += fn(i, right)
        if top >= 0 and right < N: count_queens += fn(top, right)
        if top >= 0 and left >= 0: count_queens += fn(top, left)
        if bottom < N and right < N: count_queens += fn(bottom, right)
        if bottom < N and left >= 0: count_queens += fn(bottom, left)
        if count_queens >= 1: break


    return not count_queens >= 1

"""
Funcion para resolver el problema de N queens usando la tecnica BackTracking.
@param board: tablero que representa el juego actual
@param N: dimension del tablero
@param k: columna actual
@return ans: lista que contiene las soluciones del juego.
"""
def solve(board, N, curr_col):

    # verificar si la columna actual es la ultima
    if curr_col == N: 
        print_board(board, N)
        return
    else:
        for row in range(N):
            # verificar si el movimento es valido
            if check_move(board, N, row, curr_col):
                board[row][curr_col] = 'X'
                solve(board, N, curr_col + 1)
                board[row][curr_col] = 'O'

"""
Funcion principal
@param arg: argumentos
"""
def main(args):

    N = int(args[1])
    if N == 2 or N == 3:
        print(f"No hay solucion para N={N}")
    else:
        board = [ ['O' for _ in range(N)] for i in range(N) ]
        solve(board, N, 0)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <N>" )
        exit()
    main(sys.argv)
