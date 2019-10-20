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
            pcoplayer_col = -1


        move_list = self.help.legal_move_list(board)
        
        root = chess.pgn.Game()
        root.setup(board.fen())

        best_score = [-10000] #set the bar low
        for item in move_list:
            child = chess.pgn.GameNode()
            child.parent = root
            child.move = board.parse_san(item)

            score = self.help.board_value(child.board(),player_col)
            child.comment = [child.move, score]
            root.variations.append(child)

        movespace = []
        
        for cur in root.variations:
            child_movelist = self.help.legal_move_list(cur.board())
            # print(child_movelist)

            gscore_max = -1000
            gscore = -100
            for item in child_movelist:
                gchild = chess.pgn.GameNode()
                gchild.parent = cur
                gchild.move = board.parse_san(item)
                gscore = self.help.board_value(gchild.board(),-player_col)
                if gscore > gscore_max
                    gscore_max = gscore
                    g_best_move = item
                
                total_score = 
                    
                # gchild.comment = [gchild.move, gscore]
                # root.variations.append(gchild)
            
            # # print(child_movelist)
            # for item in child_movelist:
            #     grandchild.move = 
            #     grandchild_score = self.help.board_value()

            if cur.comment[1] >= best_score[0]:
                if cur.comment[1] > best_score[0]:
                    best_score.clear()
                    movespace.clear()
                best_score.append(cur.comment[1])
                movespace.append(cur.comment[0])
        
        # for cur in root,variations:


        best_move = random.choice(movespace)
        self.turn += 1
        # print(type(best_node.move))
        if self.turn > 75:
            return chess.Move.null()
        return best_move

    class branchy:
        def __init__():
            self.node
            self.depth