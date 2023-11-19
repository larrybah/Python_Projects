#!/usr/bin/python3

"""

This is the version one of the hangman game in python.
we have a list of words and a user is asked to guess 
which of the words is in our list of words.

"""

# Words to guess from.
words = ['Beauty', 'Salutation', 'Welcome', 'Python', 'Programming']

active = True

#ask user to guess
while active:

    guess = input("Press q to quit game or Type here to play... ")

    for word in words:
        if guess == 'q':
            active = False
        elif guess == word:
            print(f"{word} You saved him!")
            break
        else:
            print(f"Guess again")
            break
