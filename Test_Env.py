# import asyncio
import random
import chess
import chess.engine
import ActionSequenceSimulating as eng1
# import SingleActionDetermining as eng2
import RandomAllpurposeNonDeterministicOutcomeManipulation as eng2
# import RandomAllpurposeNonDeterministicOutcomeManipulation as eng1
engine_1 = 'ASS'
engine_2 = 'SAD'

print("\n\t--- o ---\n\nStarting Game:\n")
if random.choice([True, False]):
    White = eng1.engine()
    Black = eng2.engine()
    print(engine_1+" is White, "+engine_2+" is Black\n")
else:
    White = eng2.engine()
    Black = eng1.engine()
    print(engine_1+" is Black, "+engine_2+" is White\n")

print("", file=open("game_stack.pgn", "w+"), end="")
print("", file=open("game_debug.txt", "w+"), end="")

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
    print("\nWhite", file=open("game_debug.txt", "a+"))
    print(board.uci(result), file=open("game_debug.txt", "a+"))
    print(board, file=open("game_debug.txt", "a+"))
    print(board.uci(result), file=open("game_stack.pgn", "a+"))

    if board.is_game_over():
        break


    result = Black.play(board, chess.engine.Limit(time=tlim))
    # move_count += 1
    # print(move_count,end='\t')
    if board.uci(result) == "0000":
        print("Black Forfeit")
        break
    board.push(result)
    print("\nBlack", file=open("game_debug.txt", "a+"))
    print(board.uci(result), file=open("game_debug.txt", "a+"))
    print(board, file=open("game_debug.txt", "a+"))
    print(board.uci(result), file=open("game_stack.pgn", "a+"))

print('Game Compled\n\n')