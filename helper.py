import chess
import re

class meth:
    def __init__(self):
        self.reg_parse = re.compile(r"(?:\w|\+|\#|\=){2,6}(?=,|\))")
        self.piece_val = { 'P': 100, 'N': 250, 'B': 300, 'R': 500, 'Q': 1000, 'K': 100000, 'p': -100, 'n': -250, 'b': -300, 'r': -500, 'q': -1000, 'k': -100000}
    def legal_move_list(self,board):
        """
        Get a list of legal moves in san notation
        """
        leg_move = board.legal_moves
        leg_move_list = re.findall(self.reg_parse,str(leg_move))
        return leg_move_list

    def board_value(self,board,player_col):
        """
        Evaluate the board position to good bad number

        player_col:
            WHITE = 1
            BLACK = -1
        """
        value = 0
        pmap = board.piece_map()
        for key in pmap:
            peice_type = pmap[key].symbol()
            value += self.piece_val[peice_type]*player_col
            # loc_val[peice_type][key]

        return value
    
    