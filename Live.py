import Score
from CurrencyRouletteGame import CurrencyRouletteGame
from GuessGame import GuessGame
from MemoryGame import MemoryGame


def welcome(name):
    print(f'Hello {name} and welcome to the world of Games(WoG).\nHere you can find many cool games to play.')


def load_game():
    games_choices = """Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
            2. Guess Game - guess a number and see if you chose like the computer
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS)"""
    print(games_choices)

    game_number = input('Enter Game number [1-3]:')
    while not game_number.isdecimal() or game_number.isdecimal() and int(game_number) not in range(1, 4):
        game_number = input('Enter Game number [1-3]:')

    game_difficulty = input('Enter Game difficulty from 1 to 5:')
    while not game_difficulty.isdecimal() or (game_difficulty.isdecimal() and int(game_difficulty) not in range(1, 6)):
        game_difficulty = input('Enter Game difficulty from 1 to 5:')

    if game_number == '1':
        if GuessGame(game_difficulty).play():
            Score.add_score(game_difficulty)
    elif game_number == '2':
        if MemoryGame(game_difficulty).play():
            Score.add_score(game_difficulty)
    else:
        if CurrencyRouletteGame(game_difficulty).play():
            Score.add_score(game_difficulty)
