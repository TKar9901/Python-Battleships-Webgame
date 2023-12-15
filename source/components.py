"""
All basic functionality across both web and command-line interfaces are developed
as functions dealing with initialisation and setup of the game as well as interacting
with external files for ships and their placements on the player's board.

Imports random and json are from the Python Standard Library so no installs are needed
and no constants were required for the basic functionality, so simplistic testing was
used to ensure functionality and reliability.
"""

## components.py
# imports
import random
import json

def print_board(board: list) -> None:
    """to print game board with clarity and consistency (in testing)

    keyword arguments:

    board -- 2d list of ship placements to print to console
    """

    for row in board:
        print(*row, sep="\t")


def initialise_board() -> list:
    """returns 2d array of size*size containing None values
    """

    with open("config.json", mode="r", encoding="utf-8") as config_file:
        size = json.load(config_file)["board_size"]

    board = [[None for i in range(size)] for j in range(size)]
    return board

# test:
# print_board(initialise_board())


def create_battleships() -> dict:
    """returns dict of {ships:size} from given file
    """

    with open("config.json", mode="r", encoding="utf-8") as config_file:
        filename = json.load(config_file)["battleship_file"]

    with open(filename , mode="r", encoding="utf-8") as file_name:
        ships = {}
        for line in file_name:
            line = line.split(":")
            ships[line[0]] = int(line[1])

    return ships

# test:
# print(create_battleships())


def place_battleships(board: list, ships: dict, method: str="simple") -> list:
    """returns board with placed ships based on given chosen method

    keyword arguments:

    board -- empty 2d list to add ship placements as given by function initialise_board,

    ships -- dictionary of ship names and sizes as given by function create_battleships,

    method -- algorithm for assigning board positions to ships, default='simple'
    """

    if method=="simple":
        i = 0
        for ship, size in ships.items():
            for size_n in range(size):
                board[i][size_n] = ship
            i += 1

    elif method=="random":
        for ship, size in ships.items():
            placed = False
            while not placed:
                orien = random.choice("hv")
                posx = random.randint(0, len(board)-1)
                posy = random.randint(0, len(board)-1)
                possible = True
            
                try:
                    for size_n in range(size):   
                        if orien == "h":
                            if board[posy][posx+size_n]:
                                possible = False
                        else:
                            if board[posy+size_n][posx]:
                                possible = False
                except IndexError:
                    pass
                else:
                    if possible:
                        for size_n in range(size):
                            if orien == "h":
                                board[posy][posx+size_n] = ship
                            else:
                                board[posy+size_n][posx] = ship
                        placed = True

    elif method=="custom":
        with open("config.json", mode="r", encoding="utf-8") as config_file:
            filename = json.load(config_file)["ship_placement_file"]

        with open(filename, mode="r", encoding="utf-8") as file_name:
            placements = json.load(file_name)

        for ship, size in ships.items():
            orien = placements[ship][2]
            posx, posy = int(placements[ship][0]), int(placements[ship][1])

            if orien == "h":
                for size_n in range(size):
                    if orien == "h":
                        board[posy][posx+size_n] = ship
                    else:
                        board[posy+size_n][posx] = ship


    return board

# test:
# print_board(place_battleships(initialise_board(), create_battleships(), method="custom"))
