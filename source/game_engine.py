"""
The original command-line interface with no opponent and only a single player targetting
unowned board of randomly placed ships is implemented here. It imports functions from
the components module and introduces functions to deal with nuances of command-line
interface such as inputting x and y coordinates and then to determine the outcome of an
attack by this coordinates on the given board.

The simple game loop provides context specific prompts and messages to the user via the
command line, including final game over statement before automatically exiting the program.

No constants where needed and no further imports are required.
"""

## game_engine.py
# imports
from components import initialise_board, create_battleships, place_battleships

def attack_outcome(coords: tuple, board:list, ships:dict) -> (bool, list, dict):
    """determines hit or miss where coords is given as (x, y) assuming
    coordinates given will follow generic standards - starting at bottom
    left at (0, 0)

    keyword arguments:

    coords -- tuple containing (x, y) as explained above,

    board -- 2d list with current ship placements,

    ships -- dictionary containing ships names and current sizes
    """

    x_coord, y_coord = coords[0], len(board)-coords[1]-1
    ship = board[y_coord][x_coord]
    if ship:
        ships[ship] -= 1
        board[y_coord][x_coord] = None
        outcome = True
    else:
        outcome = False

    return outcome, board, ships


def cli_coordinates_input(max_size) -> tuple:
    """command line input for coordinates of attack returning tuple format
    """

    x_input, y_input = max_size, max_size
    coords_dict = {
        "x": False,
        "y": False
    }

    for coord, valid in coords_dict.items():
        while not valid:
            try:
                coord_input = int(input(f"input {coord} coordinate of attack: "))
                if 0<=coord_input<max_size:
                    valid = True
                else:
                    print(f"sorry this is out of range, should be between 0 and {max_size}")

            except ValueError:
                print("sorry this is the wrong format, enter an integer")

        if coord == "x":
            x_input = coord_input
        else:
            y_input = coord_input

    return (x_input, y_input)


def simple_game_loop() -> None:
    """game loop for intermediate manual testing via command line interface
    """

    print("welcome to battleships game!")
    board = initialise_board()
    ships = create_battleships()

    print("i will place battleships on the board for you!")
    board = place_battleships(board, ships)
    # print(board)

    while sum(ships.values())>0:
        coords = cli_coordinates_input(len(board))
        outcome, board, ships = attack_outcome(coords, board, ships)
        if outcome:
            print("your shot was a hit!")
        else:
            print("sorry you missed..")

    print("that's game over!")


if __name__ == '__main__':
    simple_game_loop()
