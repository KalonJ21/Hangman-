from colorama import Fore, Back, Style
from extra_steps import hang_man, category_dict
import random 
from replit import audio

#Function for working title. 
def title():
  print(Fore.GREEN + "---------------------" + Style.RESET_ALL)
  print(Fore.RED + "Ｈ" + Fore.YELLOW + "ａ" + Fore.BLUE + "ｎ" + Fore.MAGENTA + "ｇ" + Fore.YELLOW + "ｍ" + Fore.GREEN + "ａ" + Fore.RED + "ｎ" + Fore.BLUE + "G" + Fore.GREEN + "ａ" + Fore.MAGENTA + "ｍ" + Fore.CYAN + "ｅ" + Style.RESET_ALL)
  print(Fore.GREEN + "---------------------" + Style.RESET_ALL)
  print("\n")
  print(Fore.CYAN + 'Category 1: Phrases, ' + Fore.YELLOW + 'Category 2: Anime, ' + Fore.MAGENTA + 'Category 3: People, ' + Fore.RED + 'Category 4: Movies, ' + Fore.GREEN + 'Category 5: Music' + Style.RESET_ALL)
  print("------------------------------------------------------------------")

#Function for user to select from a specifc category in category dict.
def choose_category(gamer_input):
  word = ""
  if gamer_input == 1: 
    word = random.choice(category_dict['Phrases'])
  elif gamer_input == 2:
    word = random.choice(category_dict['Anime'])
  elif gamer_input == 3:
    word = random.choice(category_dict['People'])
  elif gamer_input == 4:
    word = random.choice(category_dict['Movies'])
  elif gamer_input == 5:
    word = random.choice(category_dict['Music'])
  return word

#Function to ask for input of a character to guess the word or phrase.
def getletter():
  print()
  print("You have already printed this letter, enter another one")
  letter = input("Enter a letter: ")
  return letter

#Function to add the right characters to the word if the user guesses the character right.
def printletter(letters_in_word, letters_guessed):
  for letter in letters_in_word:
    if letter in letters_guessed: 
      print(letter + " ", end = '')
    else: 
      print("_ ", end ='')

#Function for if you ran out of guesses before you got the word or phrase.
def if_lost(word, number_mistakes, number_mistakes_allowed):
  if number_mistakes == number_mistakes_allowed:
    print(Fore.RED + "SORRY, YOU LOST.")
    print("The word was: ", end ='')
  return word


def music(song):

  source = audio.play_file(song)

  while True:
    pass
  
  return source
  