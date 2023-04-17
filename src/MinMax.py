import copy
from Score import Score
from model.Grid import Grid


class MinMax():
    def __init__(self, max_depth=5):
        self.max_depth = max_depth
        self.score = Score()

    def get_best_move(self, grid: Grid, player):
        _, best_move = self.minimax(player, 0, grid)
        return best_move

    def minimax(self, player, depth, grid: Grid):
        score = self.score.calculate_score(grid, player)

        if depth == self.max_depth or score >= 1000:
            # return game_state.evaluate(player), None
            return score, None

        if player == 'h':
            best_value = float('-inf')
            best_move = None
            stapes = self.__empty_case(grid, player)
            for move in stapes:
                # new_state = game_state.get_next_state(move, player)
                move = Grid("", cases=move)
                value, _ = self.minimax('m', depth + 1, move)
                if value > best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move
        else:
            best_value = float('inf')
            best_move = None
            stapes = self.__empty_case(grid, player)
            for move in stapes:
                # new_state = game_state.get_next_state(move, player)
                move = Grid("", cases=move)
                value, _ = self.minimax('h', depth + 1, move)
                if value < best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move

    def __empty_case(self, grid: Grid, player: str) -> list:
        empty_case = []
        for case in grid.cases:
            if case.piece == '0':
                gg = copy.deepcopy(grid)
                gg.get_case_at(case.x, case.y).piece = player
                empty_case.append(gg.cases)
                break
        return empty_case
