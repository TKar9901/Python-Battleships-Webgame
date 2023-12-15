## game_engine.py
# imports
import random
from components import print_board, initialise_board, create_battleships, place_battleships
from game_engine import attack_outcome, cli_coordinates_input

def print_ascii_board(board: list) -> None:
	"""uses print_board procedure to output board to command line interface
	using charcterised notation
	
	keyword arguments:
	board -- 2d list of current ships placements for ascii (console) output
	"""

	ascii_board = [[None for i in range(len(board))] for j in range(len(board))]

	for i, row in enumerate(board):
		for j, item in enumerate(row):
			if item:
				ascii_board[i][j] = "s"
			else:
				ascii_board[i][j] = "."

	print_board(ascii_board)


def generate_attack(board: list) -> tuple:
	"""returns random coordinates in the board for ai attack"""

	x = random.randint(0, len(board)-1)
	y = random.randint(0, len(board)-1)

	return (x, y)


def ai_opponent_game_loop() -> None:
	"""game loop for intermediate manual testing via command line interface"""

	print("welcome to battleships game!")
	players = {
		"human": {
			"board": initialise_board(),
			"ships": create_battleships()
			},
		"ai": {
			"board": initialise_board(),
			"ships": create_battleships()
			}
		}

	print("i will place your battleships using custom json file")
	print("the ai will place their battleships randomly")
	players["human"]["board"] = place_battleships(players["human"]["board"],
		players["human"]["ships"], method="custom")
	players["ai"]["board"] = place_battleships(players["ai"]["board"],
		players["ai"]["ships"], method="random")

	while sum(players["ai"]["ships"].values())>0 and sum(players["human"]["ships"].values())>0:
		print("your board looks like:")
		print_ascii_board(players["human"]["board"])

		coords = cli_coordinates_input()
		outcome, players["ai"]["board"], players["ai"]["ships"] = attack_outcome(coords,
			players["ai"]["board"], players["ai"]["ships"])
		if outcome:
			print(f"your shot was a hit!")
		else:
			print("sorry you missed..")

		coords = generate_attack(players["human"]["board"])
		outcome, players["human"]["board"], players["human"]["ships"] = attack_outcome(coords,
			players["human"]["board"], players["human"]["ships"])
		if outcome:
			print(f"the ai's shot was a hit!")
		else:
			print("the ai missed..")


	print("that's game over!")
	if players["human"]["ships"].values()==0:
		print("you lost!")
	else:
		print("you won!")


if __name__ == '__main__':
	ai_opponent_game_loop()