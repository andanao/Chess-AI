import random
import chess
import re
import helper
import chess.pgn

class engine:
    """
    Make a move based off of 1 layer deep search, just testing
    """

    def __init__(self,tlim):
        self.max_turns = 75
        self.turn = 0       
        self.tlim = tlim 
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

    def board_value(self,board,player_col):
        """
        Evaluate the board position to good bad number

        player_col:
            WHITE = 1
            BLACK = -1
        """
        try:
            value = 0
            pmap = board.piece_map()
            for key in pmap:
                peice = pmap[key]
                value += self.piece_val[peice.symbol()]*player_col

                if peice.color and player_col == 1:
                    value += self.loc_val[peice.symbol()][key]
                elif not(peice.color) and player_col == -1:
                    # value += self.loc_val[peice.symbol().capitalize()][63-key]
                    value += self.loc_val[peice.symbol().capitalize()][63 - key]
        except:
            print("it should be in this section")

        # return value
        return 2

    def play(self,board,tlim):
        if not hasattr(self,'color'):
            if board.turn == chess.WHITE:
                # print('WHITE\n\n')
                self.color = 1 #
            else:
                # print("BLACK\n\n")
                self.color = -1

        if board.fullmove_number < self.max_turns:
            root = chess.pgn.Game()
            root.setup(board.fen())
            moves = root.board().legal_moves
            for item in moves:
                root.add_variation(item)
            best_score = -100000
            possible_moves = []

            for var in root.variations:
  
            
                temp_score = self.board_value(var.board(),self.color)
                 
                if(temp_score >= best_score):
                    if(temp_score > best_score):
                        best_score = temp_score
                    possible_moves.append(var.uci())
         
            
            # print(possible_moves)
            final_move = possible_moves[random.randint(0,len(possible_moves)-1)]
            print("\t\t!!! \t "+ str(type(final_move)))
            return chess.Move.from_uci(str(final_move))
            # return chess.Move.null()
        else:
            return chess.Move.null()
    
    def get_best_variation(self,root):
        pass

