import chess
import random

class engine:
    # needs initializer
    def __init__(self):
        pass
    
    def play(self, board, tlim):
        legalmoves = board.legal_moves.tolist()
        
        random_num = random.choice(0,legalmoves.count()-1)
        optimal_play = chess.Move.from_uci(legalmoves[random_num])
        return optimal_play
