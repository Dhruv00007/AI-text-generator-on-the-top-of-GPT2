import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    words_letter = set(word)  # letter in the word
    alphabet = set(string.ascii_uppercase)  # converting it ot uppercase
    used_letter = set()  # what user has guessed
    while len(words_letter) > 0:

        print("you have used these letter: ", ' '.join(used_letter))

        word_list = [
            letter if letter in used_letter else '-' for letter in word]
        print('current word is: ', ' '.join(word_list))
        

        # getting user input

        # taking user input in upper case
        user_letter = input('guess a word: ').upper()
        if user_letter in alphabet - used_letter:  # checking if user entered letter is already in used letter
            used_letter.add(user_letter)  # then add it to empyty set
            if user_letter in words_letter:  # if user letter is in the word
                # remove it from list if it is
                words_letter.remove(user_letter)

        elif user_letter in used_letter:
            print('you already used the characrter try again')

        else:
            print("Invalid character")


hangman()
