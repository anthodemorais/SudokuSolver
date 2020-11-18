def get_next_empty(grid, empty_pos):
    for i, line in enumerate(grid):
        for j, n in enumerate(line):
            if n == 0:
                empty_pos[0] = i
                empty_pos[1] = j
                return True
    return False

def in_row(grid, n, empty_pos):
    return True if n in grid[empty_pos[0]] else False

def in_col(grid, n, empty_pos):
    col = [grid[k][empty_pos[1]] for k in range(9)]
    return True if n in col else False

# def in_box(grid, n):
#     start_line = floor(empty_pos[0] / 3) * 3
#     start_col = floor(empty_pos[1] / 3) * 3

#     box_numbers = [grid[x][y] for y in range(start_col, start_col+3) for x in range(start_line, start_line+3) if grid[x][y] != 0]
#     return True if n in box_numbers else False

def can_be_placed(grid, n, empty_pos):
    return not in_row(grid, n, empty_pos) and not in_col(grid, n, empty_pos)

def try_numbers(grid):
    empty_pos = [0, 0]
    if not get_next_empty(grid, empty_pos):
        return True

    x, y = empty_pos[0], empty_pos[1]
    start_line = (x // 3) * 3
    start_col = (y // 3) * 3

    box_numbers = [grid[x][y] for y in range(start_col, start_col+3) for x in range(start_line, start_line+3) if grid[x][y] != 0]
    for n in range(1, 10):
        if n not in box_numbers:
            if can_be_placed(grid, n, empty_pos):
                grid[x][y] = n
                if try_numbers(grid):
                    return True
                grid[x][y] = 0
    
    return False

grid_medium = [[0,0,5,3,0,0,0,0,0],
[8,0,0,0,0,0,0,2,0],
[0,7,0,0,1,0,5,0,0],
[4,0,0,0,0,5,3,0,0],
[0,1,0,0,7,0,0,0,6],
[0,0,3,2,0,0,0,8,0],
[0,6,0,5,0,0,0,0,9],
[0,0,4,0,0,0,0,3,0],
[0,0,0,0,0,9,7,0,0]]

grid_hard = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 8, 5],
    [0, 0, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 7, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 1, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 7, 3],
    [0, 0, 2, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 9],
]

if try_numbers(grid_hard):
    print(grid_hard)
else:
    print('Impossible')

# iter en for
# appeler 1x next empty