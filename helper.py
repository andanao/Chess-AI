import chess
import re

class meth:
    def __init__(self):
        pass

    @staticmethod
    def legal_move_list(board):
        leg_move = board.legal_moves
        leg_move_list = re.findall(r"\w{2,4}(?=,|\))",str(leg_move))
        return leg_move_list

    @staticmethod
    def board_value(board):
        piece_val = { 'P': 100, 'N': 250, 'B': 300, 'R': 500, 'Q': 1000, 'K': 100000}
        return value