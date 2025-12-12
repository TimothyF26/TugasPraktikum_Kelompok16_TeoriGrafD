import sys
import matplotlib.pyplot as plt

BOARD_SIZE = 8 

def is_valid_move(x, y, board):
    if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[x][y] == -1:
        return True
    return False

def get_degree(x, y, board, move_x, move_y):
    count = 0
    for i in range(8):
        nx, ny = x + move_x[i], y + move_y[i]
        if is_valid_move(nx, ny, board):
            count += 1
    return count

def print_solution_matrix(board):
    print("\nRepresentasi Matriks Langkah:")
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(f"{board[i][j]:>2}", end=" ")
        print()

def visualize_tour(board, tour_type):
    path = [None] * (BOARD_SIZE * BOARD_SIZE)
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            path[board[r][c]] = (r, c)
            
    if tour_type == 'closed':
        path.append(path[0])

    y_coords, x_coords = zip(*path) 
    
    y_coords = [-y for y in y_coords] 

    plt.figure(figsize=(6, 6))
    plt.plot(x_coords, y_coords, marker='o', markersize=5, linestyle='-')
    
    plt.plot(x_coords[0], y_coords[0], marker='*', markersize=15, color='red', label='Start')
    
    plt.title(f"Knight's Tour Visualization ({tour_type.capitalize()})")
    plt.grid(True)
    plt.axis('off')
    plt.legend()
    plt.show()

def solve_knights_tour():
    sys.setrecursionlimit(3000)
    
    while True:
        tour_type = input("Pilih jenis tour ('open' atau 'closed'): ").lower()
        if tour_type in ["open", "closed"]:
            break
        print("Input tidak valid.")

    while True:
        try:
            print(f"Masukkan posisi awal (0 - {BOARD_SIZE-1}).")
            start_x = int(input("Baris (x): "))
            start_y = int(input("Kolom (y): "))
            if 0 <= start_x < BOARD_SIZE and 0 <= start_y < BOARD_SIZE:
                break
            print("Koordinat di luar papan!")
        except ValueError:
            print("Masukkan angka integer.")

    print(f"\nSedang mencari {tour_type.capitalize()} Tour dimulai dari ({start_x}, {start_y})...")
    
    board = [[-1 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    board[start_x][start_y] = 0
    
    if not solve_tour_util(start_x, start_y, 1, board, move_x, move_y, tour_type, start_x, start_y):
        print("Solusi tidak ditemukan.")
    else:
        print(f"\nSolusi {tour_type.capitalize()} Tour ditemukan!")
        print_solution_matrix(board)
        visualize_tour(board, tour_type)

def solve_tour_util(curr_x, curr_y, move_count, board, move_x, move_y, tour_type, start_x, start_y):
    if move_count == BOARD_SIZE * BOARD_SIZE:
        if tour_type == 'open':
            return True
        elif tour_type == 'closed':
            for i in range(8):
                if (curr_x + move_x[i] == start_x) and (curr_y + move_y[i] == start_y):
                    return True
            return False

    next_moves = []
    for i in range(8):
        nx, ny = curr_x + move_x[i], curr_y + move_y[i]
        if is_valid_move(nx, ny, board):
            degree = get_degree(nx, ny, board, move_x, move_y)
            next_moves.append((degree, i, nx, ny))
    
    next_moves.sort(key=lambda x: x[0])

    for _, i, next_x, next_y in next_moves:
        board[next_x][next_y] = move_count
        if solve_tour_util(next_x, next_y, move_count + 1, board, move_x, move_y, tour_type, start_x, start_y):
            return True
        board[next_x][next_y] = -1
        
    return False

if __name__ == "__main__":
    solve_knights_tour()