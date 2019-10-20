import chess
import re

class meth:
    def __init__(self):
        self.reg_parse = re.compile(r"(?:\w|\+|\#|\=){2,6}(?=,|\))")
        self.piece_val = { 'P': 100, 'N': 250, 'B': 300, 'R': 500, 'Q': 1000, 'K': 100000, 'p': -100, 'n': -250, 'b': -300, 'r': -500, 'q': -1000, 'k': -100000}
        self.loc_val = {
            'P' : (
                 0, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 1, 1, 1, 1, 1,
                 2, 2, 2, 2, 2, 2, 2, 2,
                 2, 3, 4, 5, 5, 4, 3, 2,
                 4, 4, 5, 6, 6, 5, 4, 4,
                 5, 5, 6, 7, 7, 6, 5, 5,
                 6, 6, 7, 8, 9, 7, 6, 6,
                 7, 7, 7, 9, 9, 7, 7, 7,
                99,99,99,99,99,99,99,99,
            ),
            'N' : (
                 0, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 1, 1, 1, 1, 1,
                 2, 2,5, 2, 2,5, 2, 2,
                 3, 3, 3,10,10, 3, 3, 3,
                 4, 4, 4,10,10, 4, 4, 4,
                 5, 5, 5, 5, 5, 5, 5, 5,
                 6, 6, 6, 6, 6, 6, 6, 6,
                 7, 7, 7, 7, 7, 7, 7, 7,
                 9, 9, 9, 9, 9, 9, 9, 9,
            ), 
           'B' : (
                0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 1, 1, 1, 1, 1,
                2, 2, 2, 2, 2, 2, 2, 2,
                3, 3, 3, 3, 3, 3, 3, 3,
                4, 4, 4, 4, 4, 4, 4, 4,
                5, 5, 5, 5, 5, 5, 5, 5,
                6, 6, 6, 6, 6, 6, 6, 6,
                7, 7, 7, 7, 7, 7, 7, 7,
                9, 9, 9, 9, 9, 9, 9, 9,
            ),
            'R' : (
                0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 1, 1, 1, 1, 1,
                2, 2, 2, 2, 2, 2, 2, 2,
                3, 3, 3, 3, 3, 3, 3, 3,
                4, 4, 4, 4, 4, 4, 4, 4,
                5, 5, 5, 5, 5, 5, 5, 5,
                6, 6, 6, 6, 6, 6, 6, 6,
                7, 7, 7, 7, 7, 7, 7, 7,
                9, 9, 9, 9, 9, 9, 9, 9,
            ),
            'Q' : (
                0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 1, 1, 1, 1, 1,
                2, 2, 2, 2, 2, 2, 2, 2,
                3, 3, 3, 20, 20, 3, 3, 3,
                4, 4, 4, 20, 20, 4, 4, 4,
                5, 5, 5, 5, 5, 5, 5, 5,
                6, 6, 6, 6, 6, 6, 6, 6,
                7, 7, 7, 7, 7, 7, 7, 7,
                9, 9, 9, 9, 9, 9, 9, 9,
            ),
            'K' : (
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
            ),
        }

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
            peice = pmap[key]
            value += self.piece_val[peice.symbol()]*player_col
            if peice.color and player_col == 1:
                value += self.loc_val[peice.symbol()][key]
            elif not(peice.color) and player_col == -1:
                value += self.loc_val[peice.symbol().capitalize()][63-key]

        return value
    
    