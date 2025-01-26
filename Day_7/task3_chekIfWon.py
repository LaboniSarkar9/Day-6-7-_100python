import random

from sympy.crypto import encipher_hill

word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "-"
print(placeholder)

#TODO-1: use a while loop to let the user guess again.
game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    #TODO-2 Change the for loop so that you keep the previous correct


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "-"
    print(display)

    if "_" not in display:
        game_over = True
        print("you win!")
