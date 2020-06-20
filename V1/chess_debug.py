def print_to_debug(string):
    print(string, file=open("game_debug.txt", "a+"), end="")