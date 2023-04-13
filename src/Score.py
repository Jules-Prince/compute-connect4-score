class Score():
    
    def calculate_score(self, grid, player):
        # Calculate the score of the game based on the number of combinations of aligned tokens
        num_combinations = self.__count_combinations(grid, player)
        score = num_combinations[0]*1
        score += num_combinations[1]*10
        score += num_combinations[2]*100
        score += num_combinations[3]*1000   
        return score
    
    def __count_combinations(self, grid, player):
        grid = self.__convert(grid)
        print(grid)
        
        # Count the number of combinations of 1, 2, 3, and 4 aligned tokens in the grid
        num_combinations = [0, 0, 0, 0]  # 1, 2, 3, and 4 aligned tokens

        # Count horizontal combinations
        for j in range(6): # 0 -> 5 # column
            count = 0
            for i in range(7): # 0 -> 6 # line
                # Count horizontal combinations
                if grid[i][j] == player:
                    count += 1
                else:
                    if count > 0:
                        if count > 4:
                            count = 4
                        num_combinations[count] += 1
                        count = 0
        
        # Count vertical combinations
        for i in range(7): # 0 -> 5 # column
            count = 0
            for j in range(6): # 0 -> 6 # line
                # Count horizontal combinations
                #print("i : ", i)
                #print("j : ", j)
                #print("val : ", grid[i][j])
                if grid[i][j] == player:
                    count += 1
                else:
                    if count > 0:
                        if count > 4:
                            count = 4
                        num_combinations[count] += 1
                        count = 0

     
        return num_combinations
    
    def __convert(self, desc):
        grid_list = []
        row = []
        cpt = 0
        for case in desc:
            row.append(case)
            cpt += 1
            if cpt >= 6:
                grid_list.append(row)
                row = []
                cpt = 0
        if row:
            grid_list.append(row)
        return grid_list