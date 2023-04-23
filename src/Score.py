from src.model.Grid import Grid
from src.model.Piece import Piece

class Score:
    def calculate_score(self, grid: Grid, player: Piece):
        # Calculate the score of the game based on the number of combinations of aligned tokens
        num_combinations = self.__count_combinations(grid, player)
        score = num_combinations[0] * 1
        #print("1 : ", num_combinations[0])
        score += num_combinations[1] * 10
        #print("2 : ", num_combinations[1])
        score += num_combinations[2] * 100
        #print("3 : ", num_combinations[2])
        score += num_combinations[3] * 1000
        #print("4 : ", num_combinations[3])
        
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
        count = 0
        for i in range(13):  # column
            for j in range(7):
                x = i - j
                y = 5 - j
                if x < 0 or y < 0:
                    break
                if x <= 6:
                    
                    if grid.get_case_at(x, y).piece.value == player.value:
                        count += 1
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

    def __diag2(self, grid: Grid, player: Piece, num_combinations):
        count = 0
        for i in range(5, -7, -1): # column
            for j in range(7):
                x = i+j
                y = i-j
                if x > 6 or y < 0:
                    break
                if x >= 0:
                    
                    if grid.get_case_at(x, y).piece.value == player.value:
                        count += 1
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
            
    def __vertical(self, grid: Grid, player: Piece, num_combinations):
        count = 0
        for i in range(7):  # 0 -> 6 # column
            for j in range(6):  # 0 -> 5 # line
                # Count horizontal combinations
                if grid.get_case_at(i, j).piece.value == player.value:
                    count += 1
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
        count = 0
        # Count horizontal combinations
        for j in range(6):  # 0 -> 5 # line
            for i in range(7):  # 0 -> 6 # column
                # Count horizontal combinations
                if grid.get_case_at(i, j).piece.value == player.value:
                    count += 1
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
