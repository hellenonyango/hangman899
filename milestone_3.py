
# %%
#Asks users to guess by letter input while code runs continously 
import random 
#list of favourite fruits 
word_list = ['mango', 'passion', 'papaya', 'guava', 'oranges']

#Selects random fruits from list
generated_random_word = random.choice(word_list)

def check_guess(lower_user_letter_guess):  
  #Checks if users input is in the random word 
    if lower_user_letter_guess in generated_random_word:
        print (f'Good guess! {lower_user_letter_guess} is in the word.')
    else: 
        print(f'Sorry, {lower_user_letter_guess} is not in the word. Try again.') 

def ask_for_input():

    #Checks if users input format is correct
      while True:
        user_letter_guess = input('Enter a single letter here:' )
        #Converts the input to lower case
        lower_user_letter_guess = user_letter_guess.lower()
        if len(lower_user_letter_guess) == 1 and lower_user_letter_guess.isalpha():
            break
        else: 
          print("Invalid letter. Please, enter a single alphabetical character.") 
      check_guess(lower_user_letter_guess)

ask_for_input()


# %%
