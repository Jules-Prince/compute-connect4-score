import copy
from src.Score import Score
from src.model.Grid import Grid
from src.model.Piece import Piece
from src.model.Move import Move


class MinMax:
    def __init__(self, max_depth=4):
        self.max_depth = max_depth
        self.score = Score()

    def get_best_move(self, grid: Grid, player: Piece):
        _, best_move = self.minimax(player, 0, grid)
        new_case_to_add = grid.get_all_cases_different(best_move)[0]
        return Move(new_case_to_add.x, new_case_to_add.piece)

    def minimax(self, player: Piece, depth, grid: Grid):
        score = self.score.calculate_score(grid, player)
        #print("SCORE : ", score)

        if depth == self.max_depth or score >= 1000:
            # return game_state.evaluate(player), None
            return score, None

        if player.value == Piece.HUMAN.value:
            best_value = float('-inf')
        else:
            best_value = float('inf')
        best_move = None
        stapes = self.__empty_case(grid, player)
        
        #print("GRID DE BASE : \n", grid)
        
        #print("STAPES : \n\n")
        #for stape in stapes:
        #    print("\n")
        #    print(stape)
            
        for move in stapes:
            move = Grid("", cases=move.cases)
            value, _ = self.minimax(Piece.MACHINE if player.value == Piece.HUMAN.value else Piece.HUMAN, depth + 1, move)
            if (player.value == Piece.HUMAN.value and value > best_value) or (player.value == Piece.MACHINE.value and value < best_value):
                best_value = value
                best_move = move

            return best_value, best_move

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
                #break
                one_empty_per_column = False
        return empty_case
