from grid.Grid import Grid

class Score():
    
    
    def run(self, g):
        #grid = self.empty_case(g)
        grid = g
        print(grid)
        grid_list = self.convert(grid.brdDescription)
        print(grid_list)
        self.get_weight(grid_list)
    
    def empty_case(self, g):
        desc = g.brdDescription
        caracteres = list(desc)
        
        var = True
        for index, case in enumerate(desc):
            if (index % 6) == 0:
                var = True
            if case == '0' and var == True:
                caracteres[index] = 'x'
                var = False
        desc = "".join(caracteres)
        print(desc)
                
        return Grid(desc)
    
    def convert(self, desc):
        grid_list = []
        element = []
        for index, case in enumerate(desc):
            if (index % 6) == 0 and index != 0:
                grid_list.append(element)
                element = []
            element.append(case)
        return grid_list
         
            
                    
    def get_weight(self, grid_list, index_j, index_i, player):
        score_ref = [0, 10, 100, 1000]
        score_line = score_ref[self.line(grid_list, index_j, index_i, player)]
        
        for index_i, column in enumerate(grid_list):
            for index_j, _ in enumerate(column):
                grid_list[index_i][index_j]
        
        score_side = self.side(self, grid_list, index_j, index_i, player)
    
    def line(self, grid_list, player):
        score = 0
        for index_y, val_y in enumerate(grid_list):
            for index_x, val_x in enumerate(val_y):
                if grid_list[index_y][index_x] == player:
                    score += self.line_score(grid_list, player, index_y, index_x)
        
    def line_score(self, grid_list, player, index_y, index_x):
        print("")
        
    def verif(self, grid_list, player, index_y, index_x):            
        left = self.left_calcul(grid_list, player, index_y, index_x)
        right, index_x = self.right_calcul(grid_list, player, index_y, index_x)
        
        
    def left_calcul(self, grid_list, player, index_y, index_x):
        if index_x < 0 or grid_list[index_y][index_x] != player:
            return 0
        return 1 + self.left_calcul(grid_list, player, index_y, index_x-1)
    
    def right_calcul(self, grid_list, player, index_y, index_x):
        if index_x >= 7 or grid_list[index_y][index_x] != player:
            return 0 , index_x
        return 1 + self.left_calcul(grid_list, player, index_y, index_x+1) , index_x
        
        
        