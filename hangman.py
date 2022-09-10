import random
from words import wlist
# this function prints the hangman according to the number of the gusses the user has had 
def draw_hangman(guesses):
    hangman = ["""
                   ______
                   |    |
                   |
                   |
                   |
                   |
                _______

            """,
            """   
                   ______
                   |    |
                   |    O
                   |
                   |
                   |
                _______

            """,
            """
                   ______
                   |    |
                   |    O
                   |    |
                   |
                   |
                _______

            """,
            """ 
                   ______
                   |    |
                   |    O
                   |   \|
                   |
                   |
                _______

            """,
            """  
                   ______
                   |    |
                   |    O
                   |   \|/
                   |
                   |
                _______

            """,
            """  
                   ______
                   |    |
                   |    O
                   |   \|/
                   |   /
                   |
                _______

            """,
            """ 
                   ______
                   |    |
                   |    O
                   |   \|/
                   |   / \\
                   |
                _______

            """]
    print(hangman[guesses])


def get_word():
    word = random.choice(wlist).upper()
    return word

def play_game(word):
    word_guessed = False
    guesses_allowed = 6
    guesses = 0 
    letters_guessed = []
    words_guessed = []
    completed_word = "_"*len(word)
    instructions()
    draw_hangman(guesses)
    print (completed_word)
    print("\n")
    while not word_guessed and guesses_allowed > 0:
        print("Enter a letter to guess or a word if you're feeling brave: ")
        user_guess = input()
        user_guess = user_guess.upper()

        if user_guess.isalpha() and len(user_guess) == 1:
            if user_guess not in word and user_guess not in letters_guessed:
                print(user_guess, "is not a correct guess")
                guesses += 1
                guesses_allowed -= 1
                letters_guessed.append(user_guess)
            elif user_guess in letters_guessed:
                print(user_guess, "has already been guessed!")
            else:
                print("YAYYY!", user_guess, "is a correct guess")
                letters_guessed.append(user_guess)
                list_of_word = list(completed_word)
                indices = [i for i, letter in enumerate(word) if letter == user_guess]
                for index in indices:
                    list_of_word[index] = user_guess
                completed_word = "".join(list_of_word)
                if "_" in completed_word:
                    word_guessed = False
                else:
                    word_guessed = True

        elif user_guess.isalpha() and len(user_guess) == len(word):
            if user_guess != word:
                print("Wrong! ", user_guess, " is not the word")
                guesses += 1
                guesses_allowed -= 1
                words_guessed.append(user_guess)
            elif user_guess in words_guessed:
                print(user_guess, " has already been guessed")
            else:
                word_guessed = True 
                completed_word = word
        else:
            print("Hmmm... that was not a valid input.")
       
        draw_hangman(guesses)
        print(completed_word)
        print("\n")
    if word_guessed:
        print("YAYYY! You won the game!")
    else:
        print("...... You lost")


def instructions():
    print("Hi! Welcome to Hangman")
    print("the rules are very simple: \nA word will be chosen randomly and you will guess letters that might be in the word")
    print("If you guess correctly then you will see the letter in the coressponding spot on the blanks, but if you guess incorrectly then a body part of the hangman will be drawn!")
    print("If you think you know what the word is then you can guess it and win the game!")
    print("Careful.... you only get 6 tries at guessing the correct letter or word before the hangman is fully drawn \nGOODLUCK!!!!!")
    

#main code to run the game
play_again = "Y" 
while (play_again == "Y"):
    invalid = True
    word = get_word()
    play_game(word)
    print("Want to play again? Y or N:")
    play_again = input()
    while(not play_again.isalpha() or (not play_again.upper() == "Y" and not play_again.upper() == "N")):
        print("Invalid input try again:")
        print("Want to play again? Y or N:")
        play_again = input()
    play_again =  play_again.upper()
