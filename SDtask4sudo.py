import tkinter as tk
from tkinter import messagebox

def is_valid_move(grid, row, col, num):
    if num in grid[row]:
        return False
    
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku(grid):
    def find_empty_cell():
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return i, j
        return None, None

    def solve():
        nonlocal grid
        row, col = find_empty_cell()
        if row is None and col is None:
            return True
        
        for num in range(1, 10):
            if is_valid_move(grid, row, col, num):
                grid[row][col] = num
                if solve():
                    return True
                grid[row][col] = 0
        
        return False

    if solve():
        return grid
    else:
        return None

def solve_puzzle():
    grid = [[0]*9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            try:
                if entries[i][j].get():
                    grid[i][j] = int(entries[i][j].get())
            except ValueError:
                messagebox.showerror("Error", "Invalid input!")
                return
    
    solution = solve_sudoku(grid)
    if solution:
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, solution[i][j])
                entries[i][j].config(fg="blue")
    else:
        messagebox.showinfo("Info", "No solution exists for the given Sudoku puzzle.")

def enlarge_grid():
    new_size = 5 if entries[0][0].cget("width") == 3 else 3
    for row in entries:
        for entry in row:
            entry.config(width=new_size)

def create_grid():
    for i in range(9):
        for j in range(9):
            entry = tk.Entry(root, width=3, font=('Arial', 18), justify='center')
            entry.grid(row=i, column=j, padx=1, pady=1, ipady=5)
            if (i // 3 + j // 3) % 2 == 0:
                entry.config(bg="lightgrey")
            entries[i][j] = entry

root = tk.Tk()
root.title("Sudoku Solver")

entries = [[None]*9 for _ in range(9)]
create_grid()

solve_button = tk.Button(root, text="Solve", command=solve_puzzle)
solve_button.grid(row=9, columnspan=5)

enlarge_button = tk.Button(root, text="Enlarge", command=enlarge_grid)
enlarge_button.grid(row=9, column=5, columnspan=4)

root.mainloop()
