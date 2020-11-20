def get_boxes_numbers(grid):
    boxes_remainings = {}
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box_numbers = [grid[x][y] for y in range(j, j+3) for x in range(i, i+3) if grid[x][y] != 0]
            boxes_remainings[str(i) + str(j)] = [k for k in range(1, 10) if k not in box_numbers]
    return boxes_remainings

def get_cells_to_check(empties_pos):
    for i, empty_pos in enumerate(empties_pos):
        x, y, square_x, square_y = empty_pos[1], empty_pos[2], empty_pos[3], empty_pos[4]
        for to_check in empties_pos[:i]:
            if to_check[1] == x:
                empty_pos[6].append({1: to_check[1], 2: to_check[2]})
            elif to_check[2] == y:
                empty_pos[6].append({1: to_check[1], 2: to_check[2]})
            elif to_check[3] == square_x and to_check[4] == square_y:
                empty_pos[6].append({1: to_check[1], 2: to_check[2]})

def get_empties(grid):
    empties_pos = []
    boxes_remainings = get_boxes_numbers(grid)
    for x, line in enumerate(grid):
        for y, n in enumerate(line):
            if n == 0:
                start_line = (x // 3) * 3
                start_col = (y // 3) * 3
                box_remainings = boxes_remainings[str(start_line) + str(start_col)]
                possibles = []
                for nb in box_remainings:
                    is_valid = True
                    if not nb in line:
                        for l in range(9):
                            if nb == grid[l][y]:
                                is_valid = False
                    else:
                        is_valid = False
                    if is_valid:
                        possibles.append(nb)
                empties_pos.append({1:x, 2:y, 3:start_line, 4:start_col, 5:possibles, 6:[]})
    get_cells_to_check(empties_pos)
    return empties_pos

# def can_be_placed(grid, n, current, empties_pos):
#     for empty_pos in empties_pos:
#         if grid[empty_pos[1]][empty_pos[2]] == n:
#             if empty_pos[3] == current[3] and empty_pos[4] == current[4]:
#                     return False
#             if empty_pos[1] == current[1]:
#                     return False
#             if empty_pos[2] == current[2]:
#                     return False
#     return True

def can_be_placed(grid, n, to_check):
    for position in to_check:
        if grid[position[1]][position[2]] == n:
            return False
    return True

def try_numbers(grid, empties_pos, current_empty=0, stop_index=99):
    if current_empty >= stop_index:
        return True

    empty_pos = empties_pos[current_empty]
    # box_numbers = boxes_numbers[str(start_line) + "," + str(start_col)]
    # box_numbers = [grid[i][j] for j in range(square_y, square_y+3) for i in range(square_x, square_x+3) if grid[i][j] != 0]
    for n in empty_pos[5]:
        # if n not in box_numbers:
        # if can_be_placed(grid, n, empty_pos, empties_pos[:current_empty]):
        if can_be_placed(grid, n, empty_pos[6]):
            grid[empty_pos[1]][empty_pos[2]] = n
            if try_numbers(grid, empties_pos, current_empty=current_empty+1, stop_index=stop_index):
                return True
            grid[empty_pos[1]][empty_pos[2]] = 0
    
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
# print(get_empties(grid_medium))
empties_pos = get_empties(grid_medium)
if not try_numbers(grid_medium, empties_pos, 0, len(empties_pos)):
    print('Impossible')
# print(grid_hard)

# 379367256 function calls (310191940 primitive calls) in 401.863 seconds

#    Ordered by: internal time

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 310190708  291.995    0.000  291.995    0.000 backtracking.py:62(can_be_placed)
# 69175317/1  109.866    0.000  401.861  401.861 backtracking.py:68(try_numbers)
#         1    0.001    0.001    0.001    0.001 backtracking.py:9(get_cells_to_check)
#         1    0.000    0.000    0.001    0.001 backtracking.py:27(get_empties)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000  401.863  401.863 backtracking.py:1(<module>)
#      1205    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 backtracking.py:1(get_boxes_numbers)
#         9    0.000    0.000    0.000    0.000 backtracking.py:5(<listcomp>)
#         1    0.000    0.000  401.863  401.863 {built-in method builtins.exec}
#         9    0.000    0.000    0.000    0.000 backtracking.py:6(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 379366913 function calls (310191597 primitive calls) in 338.330 seconds

#    Ordered by: internal time

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 310190708  233.774    0.000  233.774    0.000 backtracking.py:55(can_be_placed)
# 69175317/1  104.556    0.000  338.329  338.329 backtracking.py:61(try_numbers)
#         1    0.000    0.000    0.001    0.001 backtracking.py:20(get_empties)
#         1    0.000    0.000    0.000    0.000 backtracking.py:9(get_cells_to_check)
#       863    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 backtracking.py:1(get_boxes_numbers)
#         9    0.000    0.000    0.000    0.000 backtracking.py:5(<listcomp>)
#         1    0.000    0.000  338.330  338.330 backtracking.py:1(<module>)
#         1    0.000    0.000  338.330  338.330 {built-in method builtins.exec}
#         9    0.000    0.000    0.000    0.000 backtracking.py:6(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}