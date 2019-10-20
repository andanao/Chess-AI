import chess
import random
import re

class engine:
    # needs initializer
    def __init__(self):
        pass
    
    def play(self, board, tlim):
        legalmoves = board.legal_moves.tolist()
        
        random_num = random.choice(0,legalmoves.count()-1)
        optimal_play = chess.Move.from_uci(legalmoves[random_num])
        return optimal_play

    def random_move(self,board):
        leg_move = board.legal_moves
        leg_move_str = str(leg_move)
        leg_move_list = re.findall(r"\w{2,4}(?=,|\))",leg_move_str)
        rnum = random.randint(0,len(leg_move_list)-1)
        return leg_move_list[rnum]