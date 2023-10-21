import random 
word_list = ["strawberry", "mango", "apple", "orange", "blueberry"]
word = random.choice(word_list)

guess = input("Guess a letter:")
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
