'''
Number Guessing Game.

Guesses are made until all numbers are guessed.
The game reveals whether the closest unguessed number is higher or lower than each guess.
Numbers are distinct.
Typing 'q' quits the game.
'''

import random

MIN = 0
MAX = 10
NUM_VALUES = 3

def handle_guess(guess, values):
    # This function should return a duplicate list of values
    # with the guessed value removed if it was present.
    if guess in values:
        idx = values.index(guess)
        del values[idx]
    return values
	

def find_closest(guess, values):
    # This function should return the closest value
    # to the guessed value.
    
    closeMax = values[-1]
    idx = 0
    for i in values:
        if i > guess:
            closeMax = i
            idx = values.index(closeMax)
            break;
    if (closeMax - guess < guess - values[idx - 1]):
        return closeMax
    else:
        return values[idx-1]

def run_game(values):
    # While there are values to be guessed and the user hasn't
    # quit (with 'q'), the game should wait for the user to input
    # their guess and then reveal whether the closest number is
    # lower or higher.
    print(f'Numbers are between {MIN} and {MAX} inclusive. There are {len(values)} values left.')
    guess = input('Guess: ')
    # Your code goes here.
    while (guess != 'q'):
        guess = int(guess)
        if (guess in values):
            print("You found {}! It was in the list.".format(guess))
            handle_guess(guess, values)
        else:
            closest = find_closest(guess, values)
            if closest > guess:
                position = "higher"
            else:
                position = "lower"
            print("The closest to {} is {}".format(guess, position))

        if values == []:
            print("Congratulations! You won!")
            break;

        guess = input('There are {} values left. Guess: '.format(len(values)))
    print('Thanks for playing! See you soon.')

if __name__ == '__main__':
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    run_game(values)
