import random


class GuessGame:

    def __init__(self, difficulty):
        self.difficulty = int(difficulty)

    def generate_number(self):
        secret_number = random.randrange(1, self.difficulty + 1)
        return secret_number

    def get_guess_from_user(self):
        user_guess_number = input(f'Guess the number between 1 and {self.difficulty}:')
        while not user_guess_number.isdecimal() or user_guess_number.isdecimal() \
                and int(user_guess_number) not in range(1, self.difficulty + 1):
            user_guess_number = input(f'Guess the number between 1 and {self.difficulty}:')
        return int(user_guess_number)

    def compare_results(self, secret_number, user_guess_number):
        if str(secret_number) == str(user_guess_number):
            return True
        else:
            return False

    def play(self):
        secret_number = self.generate_number()
        user_guess_number = self.get_guess_from_user()
        if self.compare_results(secret_number, user_guess_number):
            print(f'Win , secret number <{secret_number}> and your guess <{user_guess_number}>')
            return True
        else:
            print(f'Lost , secret number <{secret_number}> and your guess <{user_guess_number}>')
            return False
