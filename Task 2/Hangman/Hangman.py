# INTERMEDIATE TASK - HANGMAN GAME
from words_hangman import countries
import random

def display_hangman(attempts):
    """Display the hangman figure based on the number of incorrect attempts."""
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |
           |
        """,
    ]
    return stages[attempts]

print("#------------------------------------------------------HELLO PLAYERS WELCOME TO HANGMAN GAME-------------------------------------------------------------#")
print("\n#-----------You have to guess words based on countries, each incorrect entry can make you lose one of the man's bodypart so choose accordingly----------#")
print("\n#------------------if the man gets hanged then you LOSE, guess the correct word (letters in lowercase only) before hanged man and WIN-------------------#")

def play_hangman():
    chosen_word = random.choice(countries).lower() #we need to lowecase words for easy guessa and no hinderence
    guessed_letters = set()
    max_attempts = 6 #only 6 cases for losing man except full body
    attempts = 0
    while attempts < max_attempts:
        print(display_hangman(attempts))
        print(f"\nWord: {' '.join(letter if letter in guessed_letters else '_' for letter in chosen_word)}")
        guess = input("Enter a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess not in chosen_word:
            attempts += 1
            print(f"Incorrect! Attempts remaining: {max_attempts - attempts}")
        else:
            if all(letter in guessed_letters for letter in chosen_word):
                print(f"Congratulations! You've guessed the word: {chosen_word.capitalize()}")
                return
    print(display_hangman(attempts))
    print(f"!! you've run out of attempts. The word was: {chosen_word.capitalize()}")
def main():
    while True:
        play_hangman()
        if input("Do you want to play again? (yes/no): ").lower() != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

