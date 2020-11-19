# def get_boxes_numbers(grid):
#     boxes_numbers = {}
#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             boxes_numbers[str(i) + "," + str(j)] = [grid[x][y] for y in range(j, j+3) for x in range(i, i+3) if grid[x][y] != 0]
#     return boxes_numbers

def get_empties(grid):
    empties_pos = []
    for x, line in enumerate(grid):
        for y, n in enumerate(line):
            if n == 0:
                empties_pos.append([x, y])
    return empties_pos

# def get_next_empty(grid, empty_pos):
#     for i, line in enumerate(grid):
#         for j, n in enumerate(line):
#             if n == 0:
#                 empty_pos[0] = i
#                 empty_pos[1] = j
#                 return True
#     return False

# def in_row(grid, n, empty_pos):
#     for i in grid[empty_pos[0]]:
#         if n == i:
#             return True
#     return False

# def in_col(grid, n, empty_pos):
#     for k in range(9):
#         if n == grid[k][empty_pos[1]]:
#             return True
#     return False

# def in_box(grid, n):
#     start_line = floor(empty_pos[0] / 3) * 3
#     start_col = floor(empty_pos[1] / 3) * 3

#     box_numbers = [grid[x][y] for y in range(start_col, start_col+3) for x in range(start_line, start_line+3) if grid[x][y] != 0]
#     return True if n in box_numbers else False

def can_be_placed(grid, n, empty_pos):
    # col = empty_pos[1]
    # for i, number in enumerate(line):
    #     if n == number or n == grid[i][col]:
    #         return False
    # return True
    if n in grid[empty_pos[0]]:
        return False
    for k in range(9):
        if n == grid[k][empty_pos[1]]:
            return False
    return True
    # return not in_row(grid, n, empty_pos) and not in_col(grid, n, empty_pos)

def try_numbers(grid, empties_pos, current_empty=0, stop_index=99):
    empty_pos = [0, 0]
    if current_empty >= stop_index:
        return True
    empty_pos = empties_pos[current_empty]

    x, y = empty_pos[0], empty_pos[1]
    start_line = (x // 3) * 3
    start_col = (y // 3) * 3

    # box_numbers = boxes_numbers[str(start_line) + "," + str(start_col)]
    box_numbers = [grid[x][y] for y in range(start_col, start_col+3) for x in range(start_line, start_line+3) if grid[x][y] != 0]
    for n in range(1, 10):
        if n not in box_numbers:
            if can_be_placed(grid, n, empty_pos):
                grid[x][y] = n
                if try_numbers(grid, empties_pos, current_empty=current_empty+1, stop_index=stop_index):
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

# boxes_numbers = get_boxes_numbers(grid_medium)
empties_pos = get_empties(grid_hard)
if not try_numbers(grid_hard, empties_pos, 0, len(empties_pos)):
    print('Impossible')

# iter en for
# appeler 1x next empty
# calc 1x box_numbers

#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#  69175317  345.162    0.000  345.162    0.000 backtracking.py:1(get_next_empty)
# 69175317/1  340.492    0.000 1447.129 1447.129 backtracking.py:27(try_numbers)
#  69175316  203.209    0.000  203.209    0.000 backtracking.py:36(<listcomp>)
# 124706048  165.573    0.000  165.573    0.000 backtracking.py:14(<listcomp>)
# 307144580  155.268    0.000  558.266    0.000 backtracking.py:24(can_be_placed)
# 124706048  134.710    0.000  300.283    0.000 backtracking.py:13(in_col)
# 307144580  102.714    0.000  102.714    0.000 backtracking.py:10(in_row)
#         1    0.013    0.013    0.013    0.013 {built-in method builtins.print}
#         1    0.000    0.000 1447.142 1447.142 backtracking.py:1(<module>)
#         1    0.000    0.000 1447.142 1447.142 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disab

# 445495282 function calls (376319966 primitive calls) in 498.594 seconds

#    Ordered by: internal time

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 69175317/1  199.903    0.000  498.594  498.594 backtracking.py:58(try_numbers)
# 307144580  169.124    0.000  169.124    0.000 backtracking.py:44(can_be_placed)
#  69175316  129.567    0.000  129.567    0.000 backtracking.py:69(<listcomp>)
#         1    0.000    0.000    0.000    0.000 backtracking.py:8(get_empties)
#         1    0.000    0.000  498.594  498.594 backtracking.py:8(<module>)
#        64    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000  498.594  498.594 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}