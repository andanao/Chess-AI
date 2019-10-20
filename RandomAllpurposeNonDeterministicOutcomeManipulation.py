import chess
import random
import re

class engine:
    # needs initializer
    def __init__(self):
        pass
    
    def play(self, board, tlim):
        leg_move_list = self.legal_move_list(board)
        random_num = random.randint(0,len(leg_move_list)-1)
        optimal_play = board.push_san(leg_move_list[random_num])
        return optimal_play

    def legal_move_list(self,board):
        leg_move = board.legal_moves
        leg_move_str = str(leg_move)
        leg_move_list = re.findall(r"\w{2,4}(?=,|\))",leg_move_str)
        return leg_move_list