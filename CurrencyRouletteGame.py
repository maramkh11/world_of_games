import random

import requests  # pip install requests


class CurrencyRouletteGame:

    def __init__(self, difficulty):
        self.difficulty = int(difficulty)
        self.generated_number = random.randrange(1, 100)

    def get_money_interval(self):
        currency_rates = requests.get("https://open.er-api.com/v6/latest/USD").json()["rates"]
        usd_to_ils_rate = currency_rates["ILS"]
        interval = ((usd_to_ils_rate - (5 - self.difficulty)) * self.generated_number,
                    (usd_to_ils_rate + (5 - self.difficulty)) * self.generated_number)
        return interval

    def get_guess_from_user(self):
        user_guess_number = input(f'Guess the value of the given amount of USD {self.generated_number}:')
        while not user_guess_number.isdecimal():
            user_guess_number = input(
                f'Guess the value of the given amount of USD {self.generated_number}:[must be a number]')
        return int(user_guess_number)

    def play(self):
        interval = self.get_money_interval()
        user_guess_number = self.get_guess_from_user()
        if interval[0] <= user_guess_number <= interval[1]:
            print(f'Win , the interval is <{interval}> and your guess <{user_guess_number}>')
            return True
        else:
            print(f'Lost , the interval is <{interval}> and your guess <{user_guess_number}>')
            return False
