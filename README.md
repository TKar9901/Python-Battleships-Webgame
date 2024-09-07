# Battleships Project
Uni Y1 Solo Python Coursework

## Introduction
This project is my rendition of the popular battleships game using Flask API and provided templates to deliver the game via web interface. In particular, someone can play against an "AI" opponent to win the game by sinking all the enemy ships, as the player you are able to provide custom ship placements whereas the "AI" makes random ship placements before the game begins. You are automatically redirected through the game so this project is intended to be accessible for all users, no knowledge of web server, command line or otherwise technical knowledge is necessary to run and enjoy the game. 


## Prerequisites
Dependencies not in the installation:
- Python>=3.6
- Flask>=3.0.0


## Installation
Other dependencies provided in Python Standard Library:
- json>=2.0.9
- random
- logging

**These do not require pip install commands.**

## Getting Started Tutorial
1. Set working directory to /source folder
2. Run main.py python file
    - if using some python IDE like VSCode, click run python file
    - if using CMD, run command python main.py
3. Go to url http://127.0.0.1:5000/placement to start the game
4. You will automatically be prompted and redirected through the game, enjoy!
5. When the game is finished (a win statement is presented) exit the program from the terminal typically by pressing CTRL+C

**To run command-line interface version only:**
1. Set working directory to /source folder
2. Run mp_game_engine.py python file
    - if using some python IDE like VSCode, click run python file
    - if using CMD, run command python mp_game_engine.py
3. this version has the same functionality making use of AI opponent and "prints" the player board after every turn, enjoy!
4. the interface will automatically exit when the game is finished (a win statement is presented)


## Testing
This project can be run from a python IDE or the terminal (eg. CMD), in both cases the "console view" should provide the following message:
> Serving Flask app 'main'
>
> Debug mode: off

This allows all debug and otherwise verbose content to be shown in log.txt inside /source folder - via logging library - this is for the benefit of testing as well simplicity for the average user. You do not need to interact with this file unless you want to inspect previous runs, several logging statements have been commented out but left in the project to show its use during development and to give any user the option to debug in case of errors.

When ending the program and closing the server there will be no further messages to the "console view" however reloading the starting url given above should return:
> can't reach this page
>
> 127.0.0.1 refused to connect

This means the server has successfully been shut down, ensure you do not leave the server running as this has negative consequences of resource and memory management on your device.


## Features and Self-Review
The original functionality involves:
- firstly a command line game of battleships with simple AI opponent including:
    - randomised AI actions using random library
    - custom player ship placement via json file "placement.json"
    
    - AI attacks resulting in, contextually, ships "sinking"
    - winning statement and program end
- and to expand on this, a web interface using given templates and building on Flask API, adding:
    - Flask API infrastructure
    - html template connections
    - asyncronous programming using url requests and mapping functions to these triggers

Additional feaatures implemented:
- Within the logic:
    - ensured that the coordinate input system converts between everyday coordinates (from bottom left) to programming "coordinates" (from top left)
    - introduced checks for ensuring that if AI (randomly) doesnt picks the same board position multiple times which would otherwise slow down the game infinitely and result in immature and unrealistic game experience
    - enforced repeating hit outcome in case the player repeatedly picks the same board position multiple times, which would otherwise result in a previously sunken ship (red) to turn into an empty space (blue) which resulted in inconsistent gameplay and confusing visuals
- Within the program:
    - error handling/ checks specifically in command-line interface as this takes direct user input
    - full use of docstrings for modules and methods, providing cohesive documentation on all sections of the program
    - use of logging both during testing process to compare runs but also for simplicity of "console view" when running program
- Beyond the program:
    - config file allowing well formatted, easy to edit method to customise the app for further use/ specific needs
    - documentation using sphinx to pull docstrings and type hinting information from all modules
    - distribution files built using setup.py file providing source and build distribution files

**Self-Review:**

During the course of this project, I was able to make effective use of my resources, both digital and in-person, to develop the logic and test the functionality of the program. Unfortunately, lack of time management lead me to miss out on large portion of recording the testing/ unit testing, instead I devoted time to robust error-handling to balance this.

I chose to add certain features to the game to ensure consistency and clarity in the web interface, which I considered highly important for a GUI of a game, one of the key aspects of that being clear visuals.

I also followed good practices, refactoring and reusing my code to save time and run more efficiently such as with implementing the use of "placement.json". It was originally from the command-line interface as custom ship placements, and by overwriting it each time in web interface (in main.py module) repurposed the "place_battleships" function (in components.py module) without introducing a new subroutine to handle conversion between different data formats between my work and the html templates.


## Developer Documentation
Please see /docs/buiild/html/index.html.
This is a sphinx quick-build using the docstrings written within the python files, please be aware due to errors in the process it was not able to recognise modules which imported the components module therefore this documentation page is limited to that of the components module itself, unfortunately I was unable to resolve this.

To view specific details please see module/ function specific docstrings and type-hinting which have been provided for everything used in the project.

All modules and main code can be found in the /source folder along with the battleships.txt used to define ships and their sizes for the game and placement.json used to provide custom ship placement on the players board. These are default files defined in the config.json file which can easily be changed by the user to point to some equivalent file in the same /source directory. Please ensure you keep the same formatting style and file type for each if you choose to provide your own files. Additionally this is where log.txt can be found as discussed previously.

Sphinx documentation setup and html files can be found in /docs folder as described above, and similarly packaged distribution files can be found in /dist folder which provides compressed wheels and compressed source code, this was done using setup.py python file which can be found in root directory of this project.

## Details
- Author - Tamanna Kar
- License - MIT License
- Link to source - https://github.com/TKar9901/UoE-Project---Battleships (private repo)
