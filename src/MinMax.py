import copy
from Score import Score

class MinMax():
    def __init__(self, max_depth=5):
        self.max_depth = max_depth
        self.score = Score()

    def get_best_move(self, player, grid):
        _, best_move = self.minimax(player, 0, grid)
        return best_move

    def minimax(self, player, depth, grid):
        score = self.score.calculate_score(grid, player)
        
        if depth == self.max_depth or score >= 1000:
            #return game_state.evaluate(player), None
            return score, None

        if player == 'h':
            best_value = float('-inf')
            best_move = None
            stapes = self.__empty_case(grid, player)
            for move in stapes:
                #new_state = game_state.get_next_state(move, player)
                value, _ = self.minimax(move, 'm', depth+1)
                if value > best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move
        else:
            best_value = float('inf')
            best_move = None
            stapes = self.__empty_case(grid, player)
            for move in stapes:
                #new_state = game_state.get_next_state(move, player)
                value, _ = self.minimax(move, 'h', depth+1)
                if value < best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move
    
    
    
    def __empty_case(self, g:list[list[str]], player:str) -> list:

        empty_case = []    
        for index_y, colonne in enumerate(g):
            for index_x, val in enumerate(colonne):
                if val == '0':
                    print("g : ", g)
                    gg = copy.deepcopy(g)
                    print(gg)
                    gg[index_x][index_y] = player
                    empty_case.append(gg)
                    break
        return empty_case
    
    

    
    """
    
        
    def __init__(self):
        self.score = Score.Score()
    

    def evaluer(self, grid, level, i):

        p = ''
        if i == -1:
            p = 'm'
        elif i == 1:
            p = 'h'
                
        score = self.score.calculate_score(grid, p)
 
        if level == 4 or score >= 1000:
            return score * i
        else :
            
            
            coup_possible = self.__empty_case(grid, p)
            
            eval = i * float('inf')
            
            for coup in coup_possible:
                eval = i*min(i*eval, i*self.evaluer(coup, level+1, -i))
            
    def __empty_case(self, g:list[list[str]], player:str) -> list:

        empty_case = []    
        for index_y, colonne in enumerate(g):
            for index_x, val in enumerate(colonne):
                if val == '0':
                    print("g : ", g)
                    gg = copy.deepcopy(g)
                    print(gg)
                    gg[index_x][index_y] = player
                    empty_case.append(gg)
                    break
        return empty_case
        """