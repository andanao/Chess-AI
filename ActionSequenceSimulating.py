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
            player_col = 1 #this no worky work
        else:
            player_col = -1
        
        best_score = [-10000] #set the bar low
        root = self.help.grow_twigs(board,player_col)

        movespace = []
        #below gets the best move
        if self.turn < 1:
            test_space = []
            for cur in root.variations:
                child = self.help.grow_twigs(cur.board(),-player_col)
                for item in child.variations:
                    test_space.append(item.comment)
            print(len(test_space))

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
        if self.turn > 75:
            return chess.Move.null()
        return best_move

    # class branchy:
    #     def __init__():
    #         self.node
    #         self.depth