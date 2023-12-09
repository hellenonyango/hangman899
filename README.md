
![Static Badge](https://img.shields.io/badge/Python-3.11-%2300FFFF)

# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Hangman Project
This project is part of AiCore bootcamp where we get to build the hangman game from scratch. This project involves a combination of topics we have learnt so far on Python, Git & Git Hub and OOP. 

# Installation instructions
To install this code:
 - Fork to your remote repository 
 - Clone to your local reposority using __git clone repo URL__

# File structure of the project
- __milestone_2.py__
Contains code that picks a random word from a list of numbers. 
The second part of this file is also contains code that allows users to input a single alphabet letter and it checks if the guess is indeed an alphabet and that its only a single character.

- __milestone_3.py__
Contains code from milestone_2.py and checks if the guessed letter is in the random word. 

- __milestone_4.py__
Class Hangman is introduced. In this class we have functions that takes the guessed letter and appends to a blank list if correct. Enumarate is used to identify the letter index and replaced with the guess. We also reduce the users "live" by 1 everytime they get the guess wrong. 
- __milestone_5.py__
In this file we brings it all togther in the play_game function. Users can play the full game and get output on the progress of the game.
