import copy
import Score

class MinMax():
    def __init__(self, max_depth=5):
        self.max_depth = max_depth

    def get_best_move(self, game_state, player):
        _, best_move = self.minimax(game_state, player, 0)
        return best_move

    def minimax(self, game_state, player, depth):
        if depth == self.max_depth or game_state.is_game_over():
            return game_state.evaluate(player), None

        if player == 1:
            best_value = float('-inf')
            best_move = None
            for move in game_state.get_possible_moves():
                new_state = game_state.get_next_state(move, player)
                value, _ = self.minimax(new_state, 2, depth+1)
                if value > best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move
        else:
            best_value = float('inf')
            best_move = None
            for move in game_state.get_possible_moves():
                new_state = game_state.get_next_state(move, player)
                value, _ = self.minimax(new_state, 1, depth+1)
                if value < best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move
    
    
    
    
    
    
    
    def __init__(self):
        self.score = Score.Score()
    

    
    """
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