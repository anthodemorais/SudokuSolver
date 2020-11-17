with open('sudoku.txt', 'r') as f:
    sudoku = f.read().split("\n")
    sudoku = [s.split(",") for s in sudoku]

# put every character in its square
squares = [[], [], [], [], [], [], [], [], []]
for i, line in enumerate(sudoku):
    if i in range(3):
        for k in range(3):
            for j in range(3):
                squares[k].append(line[k * 3 + j])
    elif i in range(3, 6):
        for k in range(3):
            for j in range(3):
                squares[k + 3].append(line[k * 3 + j])
    elif i in range(6, 9):
        for k in range(3):
            for j in range(3):
                squares[k + 6].append(line[k * 3 + j])

squares = [{"remaining": [], "squares": square} for square in squares]

remaining_count = 0
for i, square in enumerate(squares):
    for j in range(1, 10):
        if not str(j) in square["squares"]:
            square["remaining"].append(j)
            remaining_count += 1

print(squares)