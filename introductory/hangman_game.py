
import random
from os import system, name

#clear the screen 
def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")




def game():
                    
    while True:                                                                 
        clear_screen()
        print("Welcome to the Hangman Game!")
        print("Guess the word below:\n")


        words = ["banana", "orange", "cherry", "watermelon"]
        word = random.choice(words)

        discovered_letters = ["_"  for letter in word]
        chances = 6
        wrong_letters = []

        while chances > 0:
            print(" ".join(discovered_letters))
            print("\nRemaining chances:", chances)
            print("Wrong letters:", " ".join(wrong_letters))

            try:
                attempt = input("\nType a letter (or 'exit' to quit):").lower()


                if attempt == "exit":
                    print("\nYou chose to exit the game. See you next time!")
                    return
                
                if not attempt.isalpha():                                           #isalpha - returns True if all the characters are alphabet letters (a-z).
                    print("Please enter only letters.")
                    continue

                if len(attempt) != 1:
                    print("Enter only one letter at a time.")
                    continue

                if attempt in discovered_letters or attempt in wrong_letters:
                    print("You have already tried this letter. Try another one!")
                    continue    

                if attempt in word:
                    
                    for index, letter in enumerate(word):
                        if attempt == letter:
                            discovered_letters[index] = letter
                        
                else:
                    chances -= 1
                    wrong_letters.append(attempt)

                if "_" not in discovered_letters:
                    print("\nCongratulations! You won! The word was:", word)
                    break

            except Exception as e:
                print(f"An error occurred: {e}")
        
        if "_" in discovered_letters:
            print("\nYou lost! The word was:",word)

        while True:
            try:
                play_again = input("\nDo you want to play again? (y/n): ").lower()
                if play_again not in ["y", "n"]:
                    print("Please type 'y' for yes or 'n' for no ")
                    continue
                break

            except Exception as e:
                print(f"An error occurred: {e}")
        
        if play_again == "n":
            print ("Thanks for playing! See you next time!")
            break


if __name__ == "__main__":
    game()
