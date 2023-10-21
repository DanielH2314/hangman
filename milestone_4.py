import random

class Hangman:

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(list(dict.fromkeys(self.word)))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess.isalpha()
        if str(guess) in self.word:
            print(f"Good guess! {guess} is in the word.")
            for element in self.word:
                if element == guess:
                    self.word_guessed[self.word.find(guess)] = guess
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.num_letters -= 1
            

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                
                

test_game = Hangman(["strawberry", "mango", "apple", "orange", "blueberry"])
test_game.ask_for_input()

