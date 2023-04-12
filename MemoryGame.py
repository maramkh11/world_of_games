import random
import time
import Utils

class MemoryGame:

    def __init__(self, difficulty):
        self.difficulty = int(difficulty)

    def generate_sequence(self):
        generated_list = []
        for index in range(0, self.difficulty):
            generated_list.append(random.randrange(1, 101))
        return generated_list

    def get_list_from_user(self):
        user_list = list(map(int, input("\nEnter the numbers : ").strip().split()))[:self.difficulty]
        return user_list

    def is_list_equal(self, generated_list, user_list):
        if generated_list == user_list:
            return True
        else:
            return False

    def display_content(self, content):
        print(f'The generated numbers are: \n{content}')
        time.sleep(0.7)
        Utils.screen_cleaner()

    def play(self):
        generated_list = self.generate_sequence()
        self.display_content(generated_list)
        user_list = self.get_list_from_user()
        if self.is_list_equal(generated_list, user_list):
            print(f'Win , generated list <{generated_list}> and your guess <{user_list}>')
            return True
        else:
            print(f'Lost , generated list <{generated_list}> and your guess <{user_list}>')
            return False
