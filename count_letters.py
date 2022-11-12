# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 11/11/2022
# Description: Write a function named count_letters that takes a string as a parameter
# and returns a dictionary that tabulates how many of each letter is in that string.

def count_letters(string):
    """Counts the value of each letter."""
    letter_dict = {}
    for letter in string.upper():
        """for loop runs through each letter of string."""
        if 'A' <= letter <= 'Z':
            """ Verifies if the letter is uppercase."""
            if not letter_dict.get(letter):
                "Verifies whether the letter is not in the dictionary."
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    return letter_dict


# print(count_letters('AaBb'))
