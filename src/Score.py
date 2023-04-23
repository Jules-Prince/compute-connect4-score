from src.model.Grid import Grid
from src.model.Piece import Piece


class Score:
    def calculate_score(self, grid: Grid, player: Piece):
        # Calculate the score of the game based on the number of combinations of aligned tokens
        num_combinations = self.__count_combinations(grid, player)
        score = num_combinations[0] * 1
        print("1 : ", num_combinations[0])
        score += num_combinations[1] * 10
        print("2 : ", num_combinations[1])
        score += num_combinations[2] * 100
        print("3 : ", num_combinations[2])
        score += num_combinations[3] * 1000
        print("4 : ", num_combinations[3])
        return score

    def __count_combinations(self, grid: Grid, player: Piece):
        # Count the number of combinations of 1, 2, 3, and 4 aligned tokens in the grid
        num_combinations = [0, 0, 0, 0]  # 1, 2, 3, and 4 aligned tokens

        self.__horizontal(grid, player, num_combinations)
        self.__vertical(grid, player, num_combinations)
        self.__diag1(grid, player, num_combinations)
        self.__diag2(grid, player, num_combinations)

        return num_combinations

    def __diag1(self, grid: Grid, player: Piece, num_combinations):
        print("DIAG 1")
        count = 0
        # print(num_combinations)
        for i in range(13):  # column
            for j in range(7):
                if i - j < 0 or 5 - j < 0:
                    break
                if i - j <= 6:
                    x = i - j
                    y = 5 - j
                    if grid.get_case_at(x, y).piece.value == player.value:
                        count += 1
                        print("COUNT : ", count)
                        print("x : ", i - j)
                        print("y : ", 5 - j)
                    else:
                        if count > 0:
                            if count > 4:
                                count = 4
                            #print("__diag1 -> ", count)
                            num_combinations[count - 1] += 1
                            count = 0
            if count > 0:
                if count > 4:
                    count = 4
                num_combinations[count - 1] += 1
                count = 0

    def __diag2(self, grid: Grid, player: Piece, num_combinations):
        print("DIAG 2")
        count = 0
        for i in range(5, -7, -1): # column
            for j in range(7):
                if i+j > 6 or i-j < 0:
                    break
                if i + j >= 0:
                    x = i+j
                    y = i-j
                    if grid.get_case_at(x, y).piece.value == player.value:
                        count += 1
                        print("COUNT : ", count)
                        print("x : ", x)
                        print("y : ", y)
                    else:
                        if count > 0:
                            if count > 4:
                                count = 4
                            #print("__diag2 -> ", count)
                            num_combinations[count - 1] += 1
                            count = 0
            if count > 0:
                if count > 4:
                    count = 4
                num_combinations[count - 1] += 1
                count = 0
            
    def __vertical(self, grid: Grid, player: Piece, num_combinations):
        print("vertcal")
        count = 0
        for i in range(7):  # 0 -> 6 # column
            for j in range(6):  # 0 -> 5 # line
                # Count horizontal combinations
                if grid.get_case_at(i, j).piece.value == player.value:
                    count += 1
                    print("COUNT : ", count)
                    print("x : ", i)
                    print("y : ", j)
                else:
                    if count > 0:
                        if count > 4:
                            count = 4
                        num_combinations[count - 1] += 1
                        count = 0
            if count > 0:
                if count > 4:
                    count = 4
                num_combinations[count - 1] += 1
                count = 0

    def __horizontal(self, grid: Grid, player: Piece, num_combinations):
        print("horizontal")
        count = 0
        # Count horizontal combinations
        for j in range(6):  # 0 -> 5 # line
            for i in range(7):  # 0 -> 6 # column
                # Count horizontal combinations
                if grid.get_case_at(i, j).piece.value == player.value:
                    count += 1
                    print("COUNT : ", count)
                    print("x : ", i)
                    print("y : ", j)
                else:
                    if count > 0:
                        if count > 4:
                            count = 4
                        num_combinations[count - 1] += 1
                        count = 0
            if count > 0:
                if count > 4:
                    count = 4
                num_combinations[count - 1] += 1
                count = 0
