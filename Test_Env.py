# import asyncio
import chess
import chess.engine
import FirstOrderOptimalLongtermStrategy as eng1
import RandomAllpurposeNonDeterministicOutcomeManipulation as eng2


print("\n\n\n\n\n\n\n")
White = eng1.engine()
Black = eng2.engine()
print("", file=open("game_stack.pgn", "w+"), end="")
print("", file=open("game_debug.pgn", "w+"), end="")


tlim = .01
board = chess.Board()

while not board.is_game_over():
    result = White.play(board, chess.engine.Limit(time=tlim))
    if board.uci(result) == "0000":
        break
    board.push(result)
    print("\nWhite", file=open("game_debug.pgn", "a+"))
    print(board.uci(result), file=open("game_debug.pgn", "a+"))
    print(board, file=open("game_debug.pgn", "a+"))
    print(board.uci(result), file=open("game_stack.pgn", "a+"))

    if board.is_game_over():
        break


    result = Black.play(board, chess.engine.Limit(time=tlim))
    if board.uci(result) == "0000":
        break
    board.push(result.move)
    print("\nBlack", file=open("game_debug.pgn", "a+"))
    print(board.uci(result.move), file=open("game_debug.pgn", "a+"))
    print(board, file=open("game_debug.pgn", "a+"))
    print(board.uci(result.move), file=open("game_stack.pgn", "a+"))

print('\n\nyou done\n\n')