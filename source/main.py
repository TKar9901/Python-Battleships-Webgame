"""
Intended as the origin of the project (entire project is showcased when this file
is run) and imports functions from all other modules in the project. This module contains
definition of the Flask API app object and functions mapping to its url requests and
triggers. These enable templates to be rendered and/or data to be requested in order to
build the logic of the battleship game for web interface.

Constants:
PLAYER_BOARD, AI_BOARD, PLAYER_SHIPS, AI_SHIPS - self explanatory
AI_ATTACKS - list of previous AI attack coords to stop it repeating attacks
PLAYER_ATTACKS - dictionary of previous player attack coords and their original outcome
to enforce consistency in the game visuals
"""

## main.py
# imports
import logging
import json
from flask import Flask, render_template, request
from components import initialise_board, create_battleships, place_battleships
from game_engine import attack_outcome
from mp_game_engine import generate_attack

FORMAT = "%(levelname)s: %(asctime)s %(message)s"
logging.basicConfig(filename="log.txt", format=FORMAT, level=logging.DEBUG)

app = Flask(__name__)

# global variables
PLAYER_BOARD = initialise_board()
AI_BOARD = initialise_board()
PLAYER_SHIPS = {}
AI_SHIPS = {}

with open("config.json", mode="r", encoding="utf-8") as config_file:
    SIZE = json.load(config_file)["board_size"]
AI_ATTACKS = [(SIZE, SIZE)]
PLAYER_ATTACKS = {}


@app.route('/', methods=["GET"])
def root() -> str:
    """handles root interface of app object by binding '/' url request via decorator
    """

    global PLAYER_BOARD, AI_BOARD, AI_SHIPS

    AI_SHIPS = create_battleships()
    PLAYER_BOARD = place_battleships(PLAYER_BOARD, PLAYER_SHIPS, method="custom")
    AI_BOARD = place_battleships(AI_BOARD, AI_SHIPS, method="random")

    return render_template("main.html", player_board=PLAYER_BOARD)


@app.route('/placement', methods=["GET", "POST"])
def placement_interface() -> (str, dict):
    """handles placement interface of app object by binding '/placement' url request
    via decorator
    """

    global PLAYER_SHIPS

    if request.method == "GET":
        PLAYER_SHIPS = create_battleships()
        return render_template("placement.html", ships=PLAYER_SHIPS,
            board_size=SIZE)

    placement_data = request.get_json()
    # logging.debug(placement_data)
    with open("placement.json", mode="w", encoding="utf-8") as placement_file:
        json.dump(placement_data, placement_file)

    return {"message": "success"}


@app.route('/attack', methods=["GET", "POST"])
def attack() -> dict:
    """handles attack interface of app object by binding '/attack' url trigger via
    decorator
    """

    global PLAYER_BOARD, PLAYER_SHIPS, AI_BOARD, AI_SHIPS, AI_ATTACKS, PLAYER_ATTACKS

    if request.args:
        coords = (int(request.args.get('x')), int(request.args.get('y')))
        # logging.debug(f"{x=}, {y=}")

        hit_outcome, AI_BOARD, AI_SHIPS = attack_outcome(coords, AI_BOARD, AI_SHIPS)
        if coords in PLAYER_ATTACKS:
            response = {"hit": PLAYER_ATTACKS[coords]}
        else:
            response = {"hit": hit_outcome}
            PLAYER_ATTACKS[coords] = hit_outcome

        ai_coords = (SIZE, SIZE)
        while ai_coords in AI_ATTACKS:
            ai_coords = generate_attack(PLAYER_BOARD)
            corrected_ai_coords = (ai_coords[0], SIZE-ai_coords[1]-1)
        AI_ATTACKS.append(ai_coords)
        response["AI_Turn"] = ai_coords
        # logging.debug(f"{ai_coords=}")

        _, PLAYER_BOARD, PLAYER_SHIPS = attack_outcome(corrected_ai_coords,
            PLAYER_BOARD, PLAYER_SHIPS)

        # logging.debug(f"{AI_SHIPS=}")
        # logging.debug(f"{PLAYER_SHIPS=}")

        if sum(AI_SHIPS.values()) == 0:
            response["finished"] = "Game Over - Player wins!"
        elif sum(PLAYER_SHIPS.values()) == 0:
            response["finished"] = "Game Over - AI wins!"

        return response


if __name__ == '__main__':
    with open("config.json", mode="r", encoding="utf-8") as config_file:
        templates = json.load(config_file)["templates_folder"]
    app.template_folder = templates
    app.run()
