import random

#from Day_7.task1_break_complex import word_list, chosen_word

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


word_list = ["aardvark", "baboon", "camel"]

# TODO-1: - Create a variable called 'lives to keep track of the set ' lives' to equal 6.
lives = 6


chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    #TODO-2 if guess is not a letter in the hose_word. Then if lives goes down to 0 then the game should stop
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose.")
    if "_" not in display:
        game_over = True
        print("you win!")

    #TODO-3 - print the ASCII art from stages tha corresponds to the current number of lives user has.

    print(stages[lives])