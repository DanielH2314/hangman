import random 
word_list = ["strawberry", "mango", "apple", "orange", "blueberry"]
word = random.choice(word_list)
print(word)

def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Oops! That is not a valid input.")
    check_guess(guess)

ask_for_input()


