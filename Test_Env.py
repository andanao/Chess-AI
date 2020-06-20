import chess
import chess.engine
import math
import time

import loopy as eng1
import loopy as eng2

# import twiggy as eng2
# import RandomTake as eng1

debug = open("game_debug.txt", "w")
stack = open("game_stack.pgn", "w")

def take_turn(board, engine):
    color = "White"
    if board.turn == chess.BLACK:
        color = "Black"
    start_time = time.time()
    result = engine.play(board, chess.engine.Limit(time=tlim))
    end_time = time.time()
    if end_time - start_time > tlim:
        print("went over time by " + str(end_time - start_time - tlim) + " sec")
    if board.uci(result) == "0000":
        print(color + " null")
        return None
    board.push(result)
    debug.write("\n\n" + color + "\n" + board.uci(result) + "\n" + str(board))
    stack.write(board.uci(result)+"\n")
    print(result)
    return board

if __name__ == '__main__':
    tlim = 1

    print("\n\n\n\n\n\n\n\t----\tStarting\t----")
    white_engine = eng1.engine(tlim)
    black_engine = eng2.engine(tlim)
    engines = {True : white_engine, False: black_engine}

    board = chess.Board()

    while not board.is_game_over():
        temp_board = take_turn(board, engines[board.turn])
        if temp_board == None:
            break
        board = temp_board
        if board.is_game_over():
            break 


    print('\n\nGG!')
    print(str(board.result())+' in '+str(math.ceil(len(board.move_stack)/2))+'\n\n')