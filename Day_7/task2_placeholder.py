import random

word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)
print(chosen_word)
# TODO-1 Create a "placeholder" with the same number of blanks as chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "-"
print(placeholder)

guess = input("Guess a letter: ").lower()

#TODO-2 Create a "display" that puts the guess letter in the right position and _ in the
# print(guess)

display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "-"
print(display)
