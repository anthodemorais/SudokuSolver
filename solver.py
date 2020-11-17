import time
start_time = time.time()

with open('sudoku.txt', 'r') as f:
    sudoku = f.read().split("\n")
    sudoku = [s.split(",") for s in sudoku]

s = [[], [], [], [], [], [], [], [], []]

# remove n-th array of empty if the number is the only one in the line or col or if there's no other possibility for this space
# eliminates possibilities for each empty space if one of the remainings can only be placed at one spot
def eliminate_possibilities(s):
    squares = s
    x_update, y_update = None, None
    should_stop = True
    for square_index, square in enumerate(squares):
        empty = square["empty"]
        unique_possibilities = []
        for i, possibilities in enumerate(empty):
            should_stop = False
            for j, possibility in enumerate(possibilities):
                flat = [item for sublist in empty for item in sublist]
                index_of_possibility = sum([len(e) for e in empty[:i]]) + j
                flat.pop(index_of_possibility)

                if not possibility in flat or len(possibilities) == 1:
                    # i-ième espace
                    # index = [i for i, n in enumerate(square["squares"]) if n == ' '][i]
                    # square["squares"][index] = str(possibility)
                    # square["remaining"].remove(int(possibility))

                    x_update, y_update = tuple(square["empty_positions"][i].split("-"))
                    x_update, y_update = int(x_update), int(y_update)
                    sudoku[x_update][y_update] = str(possibility)

                    # squares[square_index] = square
            else:
                continue # only executed if the inner loop did NOT break
            break # only executed if the inner loop DID break
        else:
            continue # only executed if the inner loop did NOT break
        break # only executed if the inner loop DID break
    # s = squares

    if not should_stop:
        s = [[], [], [], [], [], [], [], [], []]
        s = update_squares()
        eliminate_possibilities(s)
    else:
        return "Solved"



def update_squares():
    squares = [[], [], [], [], [], [], [], [], []]
    # put every character in its square
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

    squares = [{"remaining": [], "squares": square, "empty": [list() for s in square if s == " "], "empty_positions": [list() for s in square if s == " "]} for square in squares]

    # adds remaining numbers for each square
    for i, square in enumerate(squares):
        for j in range(1, 10):
            if not str(j) in square["squares"]:
                square["remaining"].append(j)

    # add every possibilities for every space for each square
    # iterate on every character of the sudoku
    # if character is a space
    # check the remaining array for the square
    # for each number in remaining check the line and col and add to empty if it can be placed

    for i, line in enumerate(sudoku):
        for j, n in enumerate(line):
            if n == " ":
                square_line = 0 if i in range(3) else (1 if i in range(3, 6) else 2)
                square_col = 0 if j in range(3) else (1 if j in range(3, 6) else 2)
                current_square = square_col + 3 * square_line

                remaining = squares[current_square]["remaining"]
                empty = squares[current_square]["empty"]

                index = empty.index(list())
                for r in remaining:
                    col = [sudoku[k][j] for k in range(9)]
                    if not str(r) in col and not str(r) in line:
                        empty[index].append(r)
                
                squares[current_square]["empty"] = empty
                squares[current_square]["empty_positions"][index] = str(i) + "-" + str(j)

    return squares

s = update_squares()
eliminate_possibilities(s)
print("--- %s seconds ---" % (time.time() - start_time))
print(sudoku)