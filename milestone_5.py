
# %%
import random 

#class definition 
class Hangman:
    #initilise the attributes of the class
    def __init__ (self, word_list, num_lives = 5):
        #word_list is the list of fruit names
        self.word_list = word_list
        # Word picked at random from list of fruit names
        self.word = random.choice(word_list)
        #A list of the letters of the word, with _ for each letter not yet guessed
        self.word_guessed = ['_' for _ in self.word]
         #num lives is the number of lives player has at the start of the game
        self.num_lives = num_lives 
        #The number of UNIQUE letters in the word that have not been guessed yet
        self.num_letters =len(set(self.word))
        #A list of the guesses that have already been tried. Set this to an empty list initially
        self.list_of_guesses = []
    
    def check_guess(self, guess):
         guess = guess.lower()
         if guess in self.word:
           print (f'Good guess! {guess} is in the word.')
           for letter in enumerate(self.word):
             if letter == guess:
               self.word_guessed[letter] = guess
               self.num_letters -= 1
         else: 
          self.num_lives -= 1 
          print(f"Sorry, {guess} is not in the word.")
          print(f"You have {self.num_lives} lives left.")
               

    def ask_for_input (self):
         #Checks if users input format is correct
      while True:
        #Converts the input to lower case
       guess = input('Enter a single letter here:' ).lower()
       if not guess.isalpha() or len(guess) != 1:
           print("Invalid letter. Please, enter a single alphabetical character.") 
       elif guess in self.list_of_guesses:
           print("You already tried that letter!")
       else: 
          self.check_guess(guess)
          self.list_of_guesses.append(guess)
          break
#Brings all the above together to allow user to play full game      
def play_game (word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters >0:
             game.ask_for_input()
        else:
            print ('you won the game')
            break

#list of favourite fruits 
word_list = ['mango', 'passion', 'papaya', 'guava', 'oranges']
play_game(word_list)

# %%
