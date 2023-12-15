### components.py
# imports
import random
import json

def print_board(board: list) -> None:
	"""to print game board with clarity and consistecy (in testing)
	
	keyword arguments:
	board -- 2d list of ship placements to print to console
	"""

	for row in board:
		print(*row, sep="\t")


def initialise_board() -> list:
	"""returns 2d array of size*size containing None values
	"""

	with open("config.json", "r") as f:
		size = json.load(f)["board_size"]

	board = [[None for i in range(size)] for j in range(size)]
	return board

# test:
# print_board(initialise_board())


def create_battleships() -> dict:
	"""returns dict of ships:size from given file
	"""

	with open("config.json", "r") as f:
		filename = json.load(f)["battleship_file"]

	with open(filename ,"r") as f:
		ships = {}
		for line in f:
			line = line.split(":")
			ships[line[0]] = int(line[1])

	return(ships)

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
			for n in range(size):
				board[i][n] = ship
			i += 1

	elif method=="random":
		for ship, size in ships.items():
			placed = False
			while not placed:
				orien = random.choice("hv")
				if orien == "h":
					try:
						posx = random.randint(0, len(board)-1)
						posy = random.randint(0, len(board)-1)
						possible = True
						for n in range(size):
							if board[posy][posx+n]:
								possible = False
					except:
						pass
					else:
						if possible:
							for n in range(size):
								board[posy][posx+n] = ship
							placed = True

				else:
					try:
						posx = random.randint(0, len(board)-1)
						posy = random.randint(0, len(board)-1)
						possible = True
						for n in range(size):
							if board[posy+n][posx]:
								possible = False
					except:
						pass
					else:
						if possible:
							for n in range(size):
								board[posy+n][posx] = ship
							placed = True

	elif method=="custom":
		with open("config.json", "r") as f:
			filename = json.load(f)["ship_placement_file"]

		with open(filename, "r") as f:
			placements = json.load(f)

		for ship, size in ships.items():
			orien = placements[ship][2]
			posx, posy = int(placements[ship][0]), int(placements[ship][1])

			if orien == "h":
				for n in range(size):
					board[posy][posx+n] = ship
			else:
				for n in range(size):
					board[posy+n][posx] = ship


	return board

# test:
# print_board(place_battleships(initialise_board(), create_battleships(), method="custom"))
