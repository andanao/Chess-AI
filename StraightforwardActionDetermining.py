import chess
import chess.pgn
import helper
import random

class engine:
    def __init__(self):
        self.turn = 0
        self.help = helper.meth()
    
    def play(self, board, tlim):
        if board.turn == chess.WHITE:
            pcol = 1 #this no worky work
        else:
            pcol = -1


        move_list = self.help.legal_move_list(board)
        
        root = chess.pgn.Game()
        root.setup(board.fen())

        best_score = [-10000] #set the bar low
        for item in move_list:
            child = chess.pgn.GameNode()
            child.parent = root
            child.move = board.parse_san(item)
            score = self.help.board_value(child.board(),pcol)
            child.comment = [child.move, score]
            root.variations.append(child)

        movespace = []
        for cur in root.variations:
            if cur.comment[1] >= best_score[0]:
                if cur.comment[1] > best_score[0]:
                    best_score.clear()
                    movespace.clear()
                best_score.append(cur.comment[1])
                movespace.append(cur.comment[0])
        

        best_move = random.choice(movespace)
        self.turn += 1
        # print(type(best_node.move))
        return best_move