
#%%
import random
#list of favourite fruits 
word_list = ['mango', 'passion', 'papaya', 'guava', 'oranges']

#Selects random fruits from list
generated_random_word = random.choice(word_list)

#prints random fruits every time function is run
print(generated_random_word)

#%%
#Iterate through whole list and returns random list each time
for name_of_fruit in word_list:
 print(random.choice(word_list))

# %%

#Asks users to guess by letter input
user_letter_guess = input('Enter a single letter here:' )

#Checks that the correct data type is entered

if len(user_letter_guess) == 1 and user_letter_guess.isalpha():
 print("Good guess!")
else: 
 print("Oops! That is not a valid input.")
# %%
