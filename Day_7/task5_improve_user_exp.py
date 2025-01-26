import random

stages = [r'''
_______
     |      |
     |      (_)
     |      \|/
     |       |
     |      | |
     |
 ____|___''', r'''
 _______
     |      |
     |      (_)
     |      \|/
     |       |
     |      | 
     |
 ____|___''', r'''
 _______
     |      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 ____|___''', r'''
 _______
     |      |
     |      (_)
     |      \|
     |       |
     |      
     |
 ____|___''', r'''
 _______
     |      |
     |      (_)
     |       |
     |       |
     |      
     |
 ____|___''', r'''
 _______
     |      |
     |      (_)
     |      
     |       
     |      
     |
 ____|___''', r'''
 _______
     |      |
     |      
     |      
     |       
     |      
     |
 ____|___''']


#TODO-1 update the wordlist to use the 'word_list' from hangman_words.py
lives = 6
#TODO-3- Import the logo from the hangman_art.py and print it at the start of game.
#module import for  word_list
word_list = ["Apple", "Boy", "Cat"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += '_'
print("word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    #Todo-6 update the code below to tell the user how many lives they have left.
    print("*******************<???>/6 LIVES LEFT*****************")
    guess = input("Guess a letter: ").lower()

    #TODO-4 if the user has entered a letter they'have already guessed, print the letter

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "-"

    print("Word to guess:" + display)

    #TODO-5: -if the letter is not in the chosen_word, print out the letter and minus life by 1.

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            # TODO-7 print you lose
            print("*******************YOU LOSE****************")

    if "-" not in display:
        game_over = True
        print("**********************YOU WIN******************")

    print(stages[lives])