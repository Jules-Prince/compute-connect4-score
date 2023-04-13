class Score():
    
    def calculate_score(self, grid):
        # Calculate the score of the game based on the number of combinations of aligned tokens
        num_combinations = self.__count_combinations(grid)
        score = num_combinations[0]*1
        score += num_combinations[1]*10
        score += num_combinations[2]*100
        score += num_combinations[3]*1000   
        return score
    
    def __count_combinations(self, grid):
        # Count the number of combinations of 1, 2, 3, and 4 aligned tokens in the grid
        num_combinations = [0, 0, 0, 0]  # 1, 2, 3, and 4 aligned tokens
        for i in range(6):
            for j in range(7):
                # Count horizontal combinations
                for k in range(1, 5):
                    if j+k > 6:
                        break
                    if grid[i][j] == grid[i][j+k]:
                        if k == 1:
                            num_combinations[0] += 1
                        elif k == 2:
                            num_combinations[1] += 1
                        elif k == 3:
                            num_combinations[2] += 1
                        else:
                            num_combinations[3] += 1
                # Count vertical combinations
                for k in range(1, 5):
                    if i+k > 5:
                        break
                    if grid[i][j] == grid[i+k][j]:
                        if k == 1:
                            num_combinations[0] += 1
                        elif k == 2:
                            num_combinations[1] += 1
                        elif k == 3:
                            num_combinations[2] += 1
                        else:
                            num_combinations[3] += 1
                # Count diagonal combinations (top-left to bottom-right)
                for k in range(1, 5):
                    if i+k > 5 or j+k > 6:
                        break
                    if grid[i][j] == grid[i+k][j+k]:
                        if k == 1:
                            num_combinations[0] += 1
                        elif k == 2:
                            num_combinations[1] += 1
                        elif k == 3:
                            num_combinations[2] += 1
                        else:
                            num_combinations[3] += 1
                # Count diagonal combinations (top-right to bottom-left)
                for k in range(1, 5):
                    if i+k > 5 or j-k < 0:
                        break
                    if grid[i][j] == grid[i+k][j-k]:
                        if k == 1:
                            num_combinations[0] += 1
                        elif k == 2:
                            num_combinations[1] += 1
                        elif k == 3:
                            num_combinations[2] += 1
                        else:
                            num_combinations[3] += 1
        return num_combinations
    
    def __string_to_grid(self, s):
        # Créer une liste vide de 6x7
        grid = [['0' for _ in range(7)] for _ in range(6)]
        # Parcourir chaque caractère de la chaîne
        for i, c in enumerate(s):
            # Calculer l'indice de ligne et de colonne correspondant
            row = i // 7
            col = i % 7

            grid[row][col] = c

        return grid