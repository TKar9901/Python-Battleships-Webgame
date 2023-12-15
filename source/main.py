##  main.py
# imports
from flask import Flask, render_template, request
from components import initialise_board, create_battleships, place_battleships
from game_engine import attack_outcome, cli_coordinates_input
from mp_game_engine import generate_attack, ai_opponent_game_loop
import json

import logging
FORMAT = "%(levelname)s: %(asctime)s %(message)s"
logging.basicConfig(filename="log.txt", format=FORMAT, level=logging.DEBUG)

app = Flask(__name__)

# global variables
player_board = initialise_board()
ai_board = initialise_board()
player_ships = {}
ai_ships = {}

with open("config.json", "r") as f:
	size = json.load(f)["board_size"]
ai_attacks = [(size, size)]
player_attacks = {}


@app.route('/', methods=["GET"])
def root() -> str:
	"""handles root interface of app object by binding '/' url request via decorator
	"""

	global player_board, player_ships, ai_board, ai_ships
	
	ai_ships = create_battleships()
	player_board = place_battleships(player_board, player_ships, method="custom")
	ai_board = place_battleships(ai_board, ai_ships, method="random")

	return render_template("main.html", player_board=player_board)
	

@app.route('/placement', methods=["GET", "POST"])
def placement_interface() -> (str, dict):
	"""handles placement interface of app object by binding '/placement' url request
	via decorator"""

	global player_board, player_ships, size

	if request.method == "GET":
		player_ships = create_battleships()
		return render_template("placement.html", ships=player_ships,
			board_size=size)

	# logging.debug("hello")
	placement_data = request.get_json()
	# logging.debug(data)
	with open("placement.json", "w") as f:
		json.dump(placement_data, f)
	# logging.debug(data)

	return {"message": "success"}

@app.route('/attack', methods=["GET", "POST"])
def attack() -> dict:
	"""handles attack interface of app object by binding '/attack' url trigger via
	decorator"""

	global player_board, player_ships, ai_board, ai_ships, ai_attacks, player_attacks, size
	
	if request.args:
		coords = (int(request.args.get('x')), int(request.args.get('y')))
		
		hit_outcome, ai_board, ai_ships = attack_outcome(coords, ai_board, ai_ships)
		if coords in player_attacks:
			response = {"hit": player_attacks[coords]}
		else:
			response = {"hit": hit_outcome}
			player_attacks[coords] = hit_outcome

		ai_coords = (size, size)
		while ai_coords in ai_attacks:
			ai_coords = generate_attack(player_board)
			corrected_ai_coords = (ai_coords[0], size-ai_coords[1]-1)
		ai_attacks.append(ai_coords)
		response["AI_Turn"] = ai_coords
		
		ai_hit_outcome, player_board, player_ships = attack_outcome(corrected_ai_coords,
			player_board, player_ships)
		
		# logging.debug(f"{ai_ships=}")
		# logging.debug(f"{player_ships=}")

		if sum(ai_ships.values()) == 0:
			response["finished"] = "Game Over - Player wins!"
		elif sum(player_ships.values()) == 0:
			response["finished"] = "Game Over - AI wins!"

		return response


if __name__ == '__main__':
	with open("config.json", "r") as f:
		templates = json.load(f)["templates_folder"]
	app.template_folder = templates
	
	app.run()