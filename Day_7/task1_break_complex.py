import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 Randomly choose  word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
print(guess)
# TODO-3 Check if the letter the user guessed (guess) is one of the letter in the chosen_word. Print "Right" if it is "worng" its not.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("wrong")
        