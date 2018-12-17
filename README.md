# bowlingGame
Simple text-based score keeping for 1 player bowling game

## Features
- keep correct score of the bowling game
- keep score of every frame as the game progresses
- restart the game at any time
- track each of the rolls in the game
- allow input of multiple roll scores together
- also track frames and roll attempts as game progresses
- print messages when strikes and spares happen
- basic tests available with some score scenarios

## Usage
1. in the same folder with the python interpreter, import the file with `from bowlingGame import *`
2. initialize the game ie. `game = bowlingGame()` - a game would have started automatically
3. make a ball roll by calling `.roll(x)` with x being the number of pins knocked down. \
    - x must be of type int, with value between 0 and 10 (pins)
4. continue to make rolls and the game will track the score for you

- check current state of the game with `.printCurrentState()`
```
----------------------
Frame Number 4
Roll Number 2
Scores per Frame: [25, 18, 8, 8, 0, 0, 0, 0, 0, 0]
Total Score: 59
----------------------
```
- check all the rolls with `.printRolls()`
```
All rolls: [10, 10, 5, 3, 8]
```
- restart the game or start a new game anytime with `.start()`

## Testing
- to test, first make sure you have pytest by installing it with pip
``` pip install -U pytest ```
- then just run pytest with `pytest -q bowlingGame.py`
- if you want to see the test output, run with `-s` > `pytest -q -s bowlingGame.py`
- Tested Scenarios
  - perfect game
  - strike / spare frame with next few rolls
  - spare in 10th frame
  - mix of strikes, spares, and normal frames
  - invalid roll input values

Also tested with 10 pin calculator - https://www.bowlinggenius.com/

## Known issues
- only announces 1 strike in 10th frame
- does not detect end of game and will allow rolls to continually get added to score
- each frame is not limited to 10 pins (roll 1 + roll 2 combined)
- ~~each roll is not bounded to 10 pins~~

## Simple improvements
- detect end of game
- ensure rolls (and 2nd rolls combined) are bounded to 10
- track strike and spare frames
- allow usage of '/' and 'X' for strikes and spares

## Other possible improvements
- support multiplayer
- more data capture like frame details, with which pins got knocked down
