# import asyncio
import random
import chess
import chess.engine
# import ActionSequenceSimulating as eng1
# import SingleActionDetermining as eng2
import RandomAllpurposeNonDeterministicOutcomeManipulation as eng2
import RandomAllpurposeNonDeterministicOutcomeManipulation as eng1
engine_1 = 'ASS'
engine_2 = 'SAD'

gamestack = open("game_stack.pgn", "w+")
debug = open("game_debug.txt", "w+")

print("\n\t--- o ---\n\nStarting Game:\n")

if random.choice([True, False]):
    White = eng1.engine()
    Black = eng2.engine()
    print(engine_1+" is White, "+engine_2+" is Black\n")
else:
    White = eng2.engine()
    Black = eng1.engine()
    print(engine_1+" is Black, "+engine_2+" is White\n")

print("", gamestack, end="")
print("", debug, end="")

# debug_file = open("game_debug.txt", "a+")
# stack_file = open("game_stack.pgn", "a+")

tlim = .01
board = chess.Board()
move_count = 0
while not board.is_game_over():
    result = White.play(board, chess.engine.Limit(time=tlim))
    # move_count += 1
    # print(move_count,end='\t')
    if board.uci(result) == "0000":
        print("White Forefeit")
        break
    board.push(result)
    print("\nWhite", debug)
    print(board.uci(result), debug)
    print(board, debug)
    print(board.uci(result), gamestack)

    if board.is_game_over():
        break


    result = Black.play(board, chess.engine.Limit(time=tlim))
    # move_count += 1
    # print(move_count,end='\t')
    if board.uci(result) == "0000":
        print("Black Forfeit")
        break
    board.push(result)
    print("\nBlack", debug)
    print(board.uci(result), debug)
    print(board, debug)
    print(board.uci(result), gamestack)

print('Game Compled\n\n')