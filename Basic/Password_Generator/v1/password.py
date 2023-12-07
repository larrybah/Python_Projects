#!/usr/bin/python3

import random

"""
A simple Password generator that generates random passwords
of 10 characters length including letters, numbers and symbols.
"""
def generate_password():

    # Define character sets.
    uppercase = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+=`-{}[]|;:'><?/~"

    # Generate Random Passwords.
    password = ""
    
    while len(password) < 10:
        
        # Choose a random character set
        character_set = random.choice([uppercase, lowercase, numbers, symbols])
        
        # Choose a random character from the chosen set
        password += random.choice(character_set)
        
    # Shuffle the password
    password = ''.join(random.sample(password, len(password)))
    return password

# Generate a random password
password = generate_password()

# Print the password
print(password)
