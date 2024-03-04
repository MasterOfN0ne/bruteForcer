# This script will generate a password file based on all possible different concatenations of 10 different strings

import itertools
import string

# Define the strings to be concatenated
strings = ['Me', 'Myself', '10', 'Irene', 'Jim', '.', '20', '11', '2007', 'Renee']

# Open the file to write the passwords to
f = open('passwordsFile.txt', 'w')

# Generate all possible combinations of the strings
for i in itertools.product(strings, repeat=3):
    # Concatenate the strings
    password = ''.join(i)
    # Write the password to the file
    f.write(password + '\n')

# Close the file
f.close()

