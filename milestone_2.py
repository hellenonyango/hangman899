
#%%
import random

#list of favourite fruits 
word_list = ['mango', 'passion', 'papaya', 'guava', 'oranges']

#Select random fruits from list
word = random.choice(word_list)

#prints random fruits every time function is run
print(word)
# %%

#Asks users to guess by letter input
guess = input('Enter a single letter here:' )

#Checks that the correct data type is entered

if len(guess) == 1 and guess.isalpha():
 print("Good guess!")
else: 
 print("Oops! That is not a valid input.")
# %%
