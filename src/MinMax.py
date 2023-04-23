import copy
from src.Score import Score
from src.model.Grid import Grid
from src.model.Piece import Piece
from src.model.Move import Move


class MinMax:
    """
        fonction Minimax(etat, joueur, profondeur_maximale)
            si la profondeur maximale est atteinte ou si l'état est un état final alors
                retourner la valeur de l'état pour le joueur Max
            sinon si le joueur est Max alors
                valeur_max = -infini
                pour chaque état possible à partir de l'état actuel faire
                    valeur = Minimax(etat_possible, Min, profondeur_maximale - 1)
                    valeur_max = max(valeur_max, valeur)
                fin pour
                retourner valeur_max
            sinon si le joueur est Min alors
                valeur_min = +infini
                pour chaque état possible à partir de l'état actuel faire
                    valeur = Minimax(etat_possible, Max, profondeur_maximale - 1)
                    valeur_min = min(valeur_min, valeur)
                fin pour
                retourner valeur_min
            fin si
        fin fonction
    """    
    
    def __init__(self, max_depth=4):
        self.max_depth = max_depth
        self.score = Score()
        self.action = None

    def get_best_move(self, grid: Grid, player: Piece):
        _, best_move = self.__run(player, 0, grid)
        #print("OK")
        #print(best_move)
        new_case_to_add = grid.get_all_cases_different(best_move)[0]
        return Move(new_case_to_add.x, new_case_to_add.piece)

    def __run(self, player: Piece, depth, grid: Grid):
        
        #print("TEST : ", player.name)
        #print(grid)
        score = self.score.calculate_score(grid, player)
        #print("SCORE : ", score)
        #print("DEPTH : ", depth)
        if depth == self.max_depth or score >= 1000:
            #print("STOP")
            return score, None
        best_move = None
        best_value = 0
        #print("0")
        stapes = self.__empty_case(grid, player)  
        #print("STAPES : \n\n")
        #for stape in stapes:
            #print("\n")
            #print(stape)  
        #print("1")    
        if player.value == Piece.MACHINE.value:
            valeur_max = float('-inf')
            for move in stapes:
                move = Grid("", cases=move.cases)
                value, _ = self.__run(Piece.HUMAN, depth + 1, move)
                #print("AFTER MACHINE : ", value)
                valeur_max = max(valeur_max, value)
                if valeur_max > best_value:
                    #print("BEST")
                    best_value = valeur_max
                    best_move = move
            #print("2")
            return valeur_max, best_move
        
        else: # Piece.HUMAN.value
            valeur_min = float('+inf')
            for move in stapes:
                move = Grid("", cases=move.cases)
                value, _ = self.__run(Piece.MACHINE, depth + 1, move)
                #print("AFTER HUMAN")
                valeur_min = min(valeur_min, value)
                if valeur_min < best_value:
                    best_value = valeur_min
                    best_move = move
            #print("3")
            return valeur_min, best_move

    def __empty_case(self, grid: Grid, player: Piece) -> list:
        empty_case = []
        one_empty_per_column = True
        for index, case in enumerate(grid.cases):
            if index % 6 == 0 and index > 0:
                one_empty_per_column = True
            if case.piece.value == Piece.BLANK.value and one_empty_per_column:
                gg = copy.deepcopy(grid)
                gg.get_case_at(case.x, case.y).piece = player
                empty_case.append(gg)
                one_empty_per_column = False
        return empty_case
