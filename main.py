#Randomizes words from a selected category.
import random
from replit import audio

#imports of needed code (words, hangman model, etc).
from extra_steps import hang_man, category_dict
# !pip install colorama
from colorama import Fore, Back, Style
from replit import audio

#imports functions for code
from functions import title, choose_category, getletter, music, printletter, if_lost


def main():

    # this_song = "remixpvztheme.mp3"
    # my_music = music(this_song)
    # print(my_music)
    
    #constants
    number_mistakes = 0
    letters_guessed = []
    #the number of wrong guesses you can make is equal to the length of the hangman figure.
    number_mistakes_allowed = len(hang_man)
    # word = random.choice(words)
    wrong_letters = []
    #Prints out the title for the hangman game.
    title()
    gamer_input = int(input("What category would you like to choose: \n"))

    #The word is initialized as the one randomly chosen from input of the user.
    word = choose_category(gamer_input)
    #word is made into a list to iterate over.
    letters_in_word = list(word)
    print("\n")
    print("This word has " + str(len(letters_in_word)) + " letters.")

    #Nested while loop to keep track of correct and incorrect guesses, along with adding to the word.
    while number_mistakes < number_mistakes_allowed:
        print()
        print("Wrong letters: ", end='')
        for letter in wrong_letters:
            print(letter + ',', end='')

        print()
        print("Guesses left: " +
              str(number_mistakes_allowed - number_mistakes))
        character_user = input("Enter a character: ")

        while character_user in letters_guessed or character_user in wrong_letters:
            character_user = getletter()

        if character_user not in letters_in_word:
            number_mistakes += 1
            wrong_letters.append(character_user)

        print()
        print('Word: ', end='')

        for letter in letters_in_word:
            if character_user == letter:
                letters_guessed.append(character_user)

        printletter(letters_in_word, letters_guessed)

        if number_mistakes:
            print()
            print(hang_man[number_mistakes - 1])
        print("\n")
        print(Fore.MAGENTA +
              "--------------------------------------------------------" +
              Style.RESET_ALL)

        #win scenario
        if len(letters_guessed) == len(letters_in_word):
            print("\n")
            print(Fore.GREEN + "CONGRATS, YOU WON!!!  : ) ")
            break

    #lose scenario
    you_lose = if_lost(word, number_mistakes, number_mistakes_allowed)
    print(you_lose)


if __name__ == "__main__":
    main()
