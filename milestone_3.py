
# %%
#Asks users to guess by letter input while code runs continously 
import random 
#list of favourite fruits 
word_list = ['mango', 'passion', 'papaya', 'guava', 'oranges']

#Selects random fruits from list
word = random.choice(word_list)

def check_guess(guess):  
  #Checks if users input is in the random word 
    if guess in word:
        print (f'Good guess! {guess} is in the word.')
    else: 
        print(f'Sorry, {guess} is not in the word. Try again.') 

def ask_for_input():

    #Checks if users input format is correct
      while True:
        guess = input('Enter a single letter here:' )
        if len(guess) == 1 and guess.isalpha():
            break
        else: 
          print("Invalid letter. Please, enter a single alphabetical character.") 
      check_guess(guess)

ask_for_input()


# %%
