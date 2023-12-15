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

	x, y = coords[0], len(board)-coords[1]-1
	ship = board[y][x]
	if ship:
		ships[ship] -= 1
		board[y][x] = None
		outcome = True
	else:
		outcome = False

	return outcome, board, ships


def cli_coordinates_input() -> tuple:
	"""command line input for coordinates of attack returning tuple format"""

	x = int(input("input x coordinate of attack: "))
	y = int(input("input y coordinate of attack: "))

	return (x, y)


def simple_game_loop() -> None:
	"""game loop for intermediate manual testing via command line interface"""

	print("welcome to battleships game!")
	board = initialise_board()
	ships = create_battleships()

	print("i will place battleships on the board for you!")
	board = place_battleships(board, ships)
	print(board)

	while sum(ships.values())>0:
		coords = cli_coordinates_input()
		outcome, board, ships = attack_outcome(coords, board, ships)
		if outcome:
			print(f"your shot was a hit!")
		else:
			print("sorry you missed..")

	print("that's game over!")


if __name__ == '__main__':
	simple_game_loop()