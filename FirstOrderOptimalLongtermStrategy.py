import chess
# done 10:12
# moveset = ["d2d4", "e1c3", "c1f4", "c3c7"]

class engine:
    # needs initializer
    def __init__(self):
        self.moveset = ["e2e4", "d1f3", "f1c4", "f3f7"]
        self.turn = 0
    
    def play(self, board, tlim):
        legalmoves = board.legal_moves
        if self.turn < 4 and chess.Move.from_uci(self.moveset[self.turn]) in legalmoves:
            optimal_play = chess.Move.from_uci(self.moveset[self.turn])
        else:
            optimal_play = chess.Move.null()
        self.turn += 1
        print(self.turn)
        return optimal_play
