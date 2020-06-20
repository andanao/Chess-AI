import random
import chess
import re
import helper

class engine:
    """
    Make a random move, just testing
    """

    def __init__(self):
        self.turn = 0        
        self.reg_parse = re.compile(r"(?:\w|\+|\#|\=|\-){2,6}(?=,|\))")
        self.piece_val = { 'P': 10, 'N': 25, 'B': 30, 'R': 50, 'Q': 100, 'K': 1000, 'p': -10, 'n': -25, 'b': -30, 'r': -50, 'q': -100, 'k': -1000}
        self.loc_val = {
            'P' : (
                1,  1,  1,  1,  1,  1,  1,  1,
                2,  2,  2,  3,  3,  2,  2,  2,
                2,  2,  3,  4,  4,  3,  2,  2,
                3,  3,  4,  5,  5,  4,  3,  3,
                3,  3,  4,  5,  5,  4,  3,  3,
                2,  2,  3,  4,  4,  3,  2,  2,
                10, 10, 10, 10, 10, 10, 10, 10,
                # 69, 69, 69, 69, 69, 69, 69, 69, 
            ),
            'N' : (
                 1,	1,	1,	1,	1,	1,	1,	1,
                2,	2,	2,	3,	3,	2,	2,	2,
                2,	2,	3,	4,	4,	3,	2,	2,
                3,	3,	4,	5,	5,	4,	3,	3,
                3,	3,	4,	5,	5,	4,	3,	3,
                2,	2,	3,	4,	4,	3,	2,	2,
                2,	2,	2,	3,	3,	2,	2,	2,
                1,	1,	1,	1,	1,	1,	1,	1, 
            ), 
           'B' : (
                1,	1,	1,	1,	1,	1,	1,	1,
                2,	2,	2,	3,	3,	2,	2,	2,
                2,	2,	3,	4,	4,	3,	2,	2,
                3,	3,	4,	5,	5,	4,	3,	3,
                3,	3,	4,	5,	5,	4,	3,	3,
                2,	2,	3,	4,	4,	3,	2,	2,
                2,	2,	2,	3,	3,	2,	2,	2,
                1,	1,	1,	1,	1,	1,	1,	1, 
            ),
            'R' : (
                1,	1,	1,	1,	1,	1,	1,	1,
                2,	2,	2,	3,	3,	2,	2,	2,
                2,	2,	3,	4,	4,	3,	2,	2,
                3,	3,	4,	5,	5,	4,	3,	3,
                3,	3,	4,	5,	5,	4,	3,	3,
                2,	2,	3,	4,	4,	3,	2,	2,
                2,	2,	2,	3,	3,	2,	2,	2,
                1,	1,	1,	1,	1,	1,	1,	1, 
            ),
            'Q' : (
                1,	1,	1,	1,	1,	1,	1,	1,
                2,	2,	2,	3,	3,	2,	2,	2,
                2,	2,	3,	4,	4,	3,	2,	2,
                3,	3,	4,	5,	5,	4,	3,	3,
                3,	3,	4,	5,	5,	4,	3,	3,
                2,	2,	3,	4,	4,	3,	2,	2,
                2,	2,	2,	3,	3,	2,	2,	2,
                1,	1,	1,	1,	1,	1,	1,	1, 
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

    def play(self,board,tlim):
        if self.turn <75:
            mov_list = self.legal_move_list(board)
            random_num = random.randint(0,len(mov_list)-1)
            try:
                optimal_play = board.parse_san(mov_list[random_num])
            except:
                print("something broke in the randomizer")
                print(board)
                print("tried: "+mov_list[random_num])
                pass