import time
start_time = time.time()

class Solver:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            sudoku = f.read().split("\n")
            default_sudoku = [s.split(",") for s in sudoku]
            self.sudoku = default_sudoku
            self.default_sudoku = default_sudoku

            self.randoms_to_try = []
            self.randoms_positions = []
            self.randoms_tested = []

            self.s = [[], [], [], [], [], [], [], [], []]
            self.versions = [self.default_sudoku]

    # remove n-th array of empty if the number is the only one in the line or col or if there's no other possibility for this space
    # eliminates possibilities for each empty space if one of the remainings can only be placed at one spot
    def eliminate_possibilities(self, randoms_index=0):
        squares = self.s
        x_update, y_update = None, None
        # should_stop = True
        nothing_changed = True
        for square_index, square in enumerate(squares):
            empty = square["empty"]
            for i, possibilities in enumerate(empty):
                # should_stop = False
                for j, possibility in enumerate(possibilities):
                    flat = [item for sublist in empty for item in sublist]
                    index_of_possibility = sum([len(e) for e in empty[:i]]) + j
                    flat.pop(index_of_possibility)

                    if not possibility in flat or len(possibilities) == 1:
                        nothing_changed = False
                        # i-ième espace
                        # index = [i for i, n in enumerate(square["squares"]) if n == ' '][i]
                        # square["squares"][index] = str(possibility)
                        # square["remaining"].remove(int(possibility))
                        x_update, y_update = tuple(square["empty_positions"][i].split("-"))
                        x_update, y_update = int(x_update), int(y_update)
                        self.sudoku[x_update][y_update] = str(possibility)

                        # squares[square_index] = square
                else:
                    continue # only executed if the inner loop did NOT break
                break # only executed if the inner loop DID break
            else:
                continue # only executed if the inner loop did NOT break
            break # only executed if the inner loop DID break
        # s = squares

        result = self.check_winner()
        # print(result)

        if result == 'solved':
            return result
        elif result == 'not finished' and not nothing_changed:
            self.prev_sudoku = self.sudoku
            self.s = [[], [], [], [], [], [], [], [], []]
            self.update_squares()
            self.eliminate_possibilities(randoms_index)
        elif (result == 'not finished' and nothing_changed) or result == 'error':
            if result == 'not finished' and nothing_changed:
                self.s = [[], [], [], [], [], [], [], [], []]
                self.update_squares(True)
            for i, random in enumerate(self.randoms_to_try[randoms_index:]):
                for j, number in enumerate(random):
                    x_update, y_update = tuple(self.randoms_positions[randoms_index].split("-"))
                    x_update, y_update = int(x_update), int(y_update)
                    self.sudoku[x_update][y_update] = str(number)

                    self.s = [[], [], [], [], [], [], [], [], []]
                    self.update_squares()
                    self.eliminate_possibilities(randoms_index=randoms_index+1)
                    result = self.check_winner()
                    if result == "solved":
                        return result
                    elif result == "error":
                        self.sudoku = self.versions[randoms_index]
                
                    self.randoms_tested[randoms_index] = self.randoms_tested[randoms_index] + 1
        # else:
        #     if not should_stop:
        #         s = [[], [], [], [], [], [], [], [], []]
        #         s = update_squares()
        #         eliminate_possibilities(s)
        #     else:
        #         return "Solved"



    def update_squares(self, should_append_to_randoms=False):
        squares = [[], [], [], [], [], [], [], [], []]
        # put every character in its square
        for i, line in enumerate(self.sudoku):
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
        lowest_possibilities_count = 99
        lowest_possibilities_numbers = []
        lowest_possibilities_positions = ""
        for i, line in enumerate(self.sudoku):
            for j, n in enumerate(line):
                if n == " ":
                    square_line = 0 if i in range(3) else (1 if i in range(3, 6) else 2)
                    square_col = 0 if j in range(3) else (1 if j in range(3, 6) else 2)
                    current_square = square_col + 3 * square_line

                    remaining = squares[current_square]["remaining"]
                    empty = squares[current_square]["empty"]

                    index = empty.index(list())
                    for r in remaining:
                        col = [self.sudoku[k][j] for k in range(9)]
                        if not str(r) in col and not str(r) in line:
                            empty[index].append(r)
                    
                    if len(empty[index]) < lowest_possibilities_count:
                        lowest_possibilities_count = len(empty[index])
                        lowest_possibilities_numbers = empty[index]
                        lowest_possibilities_positions = str(i) + "-" + str(j)
                    
                    squares[current_square]["empty"] = empty
                    squares[current_square]["empty_positions"][index] = str(i) + "-" + str(j)

        if lowest_possibilities_count != 99 and should_append_to_randoms:
            self.randoms_to_try.append(lowest_possibilities_numbers)
            self.randoms_tested.append(0)
            self.randoms_positions.append(lowest_possibilities_positions)
            self.versions.append(self.sudoku)

        self.s = squares

    def check_winner(self):
        for i, line in enumerate(self.sudoku):
            for j, n in enumerate(line):
                if n == " ":
                    return "not finished" 
                col = [self.sudoku[k][j] for k in range(9)]
                if n in col or n in line:
                    return "error"
        return "solved"

solver = Solver("./sudokus/sudoku2.txt")
solver.update_squares()
solver.eliminate_possibilities()
print("--- %s seconds ---" % (time.time() - start_time))
print(solver.sudoku)