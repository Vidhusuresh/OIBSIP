

import random
import string

#length and character declaration
length = int(input("Enter password length: "))
use_letters = input("Include letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'


chars = ''
if use_letters != 0:
    chars += string.ascii_letters
if use_numbers != 0:
    chars += string.digits
if use_symbols != 0:
    chars += string.punctuation

#password generation
if not chars:
    print("Error: You must choose at least one character type.")
else:
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated password:", password)
