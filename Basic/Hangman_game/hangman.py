#!/usr/bin/python3

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
