import random
word_list = ["strawberry", "mango", "apple", "orange", "blueberry"]

class Hangman:

    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(list(dict.fromkeys(self.word)))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        """
        This function checks if the letter guessed is in the word.
        
        This function first checks that the letter is found in the word.
        If so, it informs the player this is the case.
        It then replaces the '_' in the word being guessed with the correspoding letter.
        After this, the number of letters left to guess is reduced by one.
        If the letter is not in the word then the player is informed and they lose a life.
        """
        guess.isalpha()
        if str(guess) in self.word:
            print(f"Good guess! {guess} is in the word.")
            for element in self.word:
                if element == guess:
                    self.word_guessed[self.word.find(guess)] = guess
            self.num_letters -= 1
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            

    def ask_for_input(self):
        """
        This function asks the user the guess a letter.
        
        The player enters a letter. The function first checks if this is a single character and a letter in the alphabet.
        If this is not the case the player is informed.
        If the letter is a single character then the function is ran to check whether this letter is in the word.
        Finally the function adds the letter to the list of guessed letters, ensuring the player can only guess a specific letter once. 
        """
        guess = input("Guess a letter: ")
        if guess.isalpha() == False or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.list_of_guesses.append(guess)
            self.check_guess(guess)
                

def play_game(word_list):
    """
    This function plays a game of Hangman 
    
    This is a function that chooses a random word from the list passed to the function and starts a game with five lives.
    The function displays how many characters are in the word and asks the player to continuously guess a letter. 
    They are told if the letter is in the word or not. Each time they guess incorrectly they lose a life.
    If the player runs out of lives the game finishes. 
    If the player guesses all the characters, they win the game.
    """
    game = Hangman(word_list = word_list, num_lives = 5)
    print(game.word_guessed)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            exit()
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            exit()

play_game(word_list)