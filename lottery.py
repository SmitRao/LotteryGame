'''Lottery - Guessing Game'''

import random
import time
import csv
import game_functions
import lottery_code
from typing import Dict, List

print('\n\
       ----------------------\n\
       Developed by Smit Rao.\n\
       ----------------------\n\
       LOOT     THE     LOTTO\n\
       ----------------------\
\n')

time.sleep(2)



print('\n***   INSTRUCTIONS & CONDITIONS   ***\n\n\
\
Play responsibly, know your limits.\n')

time.sleep(2)

print('\
\n\
In this lottery game, you must guess a \n\
random number from [0, 100] inclusive. \n\
You will get five (5) chances to guess. \n\
\nPRIZE.............\
..............  $ 10\n\
COST PER SESSION........\
.........  $ 1\n\
CHANCES OF WINNING.....\
....  1  in  20\n\n\
If your guess is correct at least once, you\n\
will receive a code which you must present \n\
to the developer (Smit Rao) for the prize.\n\
\nIn order to claim the prize, you must accurately\n\
follow all prompts for personal details as well as\n\
instructions for claiming the reward. \n\
\nIn addition, be advised that for the duration of\n\
the lottery game, you must be supervised by either\n\
the developer (Smit Rao) or a selected referee\n\
(witness) present to administer the lottery.\n\
\n\n\
')

time.sleep(5)

CONSENT = game_functions.clean_words(input('\
Commencing this game obliges you\n\
to make a payment of one ($1) dollar.\n\n\
Do you agree to pay the developer\n\
this amount by the end of the game?\n\
\n( Y / N ) > ')) + ' '


while CONSENT[0] != 'Y':
    CONSENT = game_functions.clean_words(input('\
    \n\n\n\n\nTo continue, please agree to our terms.\n\
Otherwise, please close this window.\n\
    \n( Y / N ) > ')) + ' '

PLAYER_FIRST_NAME = game_functions.clean_words(input('\
\n\n\nPlease enter your first name: \n> '))
while PLAYER_FIRST_NAME == '':
    PLAYER_FIRST_NAME = game_functions.clean_words(input('\
\n\nWe want to know who is playing. \n\
We request your first name: \n> '))

PLAYER_LAST_NAME = game_functions.clean_words(input('\
\n\n\n\nPlease enter your last name: \n> '))
while PLAYER_LAST_NAME == '':
    PLAYER_LAST_NAME = game_functions.clean_words(input('\
\n\nWe want to know who is playing. \n\
We request your last name: \n> '))
    
PLAYER_NAME = PLAYER_FIRST_NAME + ' ' + PLAYER_LAST_NAME

PLAYER_EMAIL = input('\n\n\n\n\nPlease enter your email: \n> ')
while '@' not in PLAYER_EMAIL:
    PLAYER_EMAIL = input('\nPlease enter a valid email: \n> ')

print('\n\n\n\n\n\n\
Thank you for the information,', PLAYER_NAME)
print('\nThe game will start in thirty (30) seconds.\n\
\nPlease pay the $1 fee for this session immediately if\n\
you have not yet done so.\n\n\
At this point, if you do not wish to pay, you\n\
may not play. Please close the window to quit.\n\
\nOtherwise, enjoy!\n\n[DO NOT PRESS ANY KEY]\n\n\n')
for n in range(30):
    print(30 - n)
    time.sleep(1)
print('\n\nStarting... Ready? Go!')
time.sleep(1.4)

WINNING_CODE = '\n'.join(lottery_code.\
get_random_code(50).split('.'))

print('\n\n\n\n*************************\
*******************')
print('Start Time:', game_functions.clean_time())
winner = False
win = False
random_numbers = []
player_numbers = []

chances = ['First', 'Second', \
'Third', 'Fourth', 'Fifth']

for n in range(5):
    RANDOM = random.randint(0, 100) # 1 - test
    random_numbers.append(RANDOM)
    print('\n\n\n\n\n\n\n')
    print(chances[n], 'Guess')
    print('-------------')
    GUESS = input('Enter your guess (0 - 100): ')
    if GUESS.isnumeric():
        GUESS = int(GUESS)    
    while type(GUESS) != int or GUESS > 100 or GUESS < 0:
        GUESS = input('Please enter a valid guess (0 - 100): ')
        if GUESS.isnumeric():
            GUESS = int(GUESS)
    player_numbers.append(GUESS)
    winner = (RANDOM == GUESS)
    if winner:
        win = True
    print('\n')
    print(winner)
    print('\n\n')

print('\n\n\n\n\n\n\nWinning numbers (ordered):', random_numbers)
print('Your numbers (ordered):', player_numbers)


if win:
    print('\n\n\n')
    print(PLAYER_FIRST_NAME, ':')
    print('\n\
Congratulations on your win! Please \n\
redeem your prize within twenty-four \n\
(24) hours using the following code:\n')
    print(WINNING_CODE, '\n\n\n\n')
    print('\nPlease present your code to the developer\n\
(Smit Rao) or email it as follows:\n\
TO: info@xprescolor.com\n\
CC: smit@smitrao.co, rao.smit.2@gmail.com,\n\
smit.rao@mail.utoronto.ca\n\
\n\n\nFailure to follow these instructions\n\
within twenty-four (24) hours of your\n\
win may result in a loss of your prize.\n\
\n\nYour patronage and understanding\n\
is sincerely appreciated. \
', '\n')

elif not win:
    print('\n\n\n')
    print(PLAYER_FIRST_NAME, ':')
    print('\n\
Unfortunately your numbers did not\n\
match our winning numbers. \n\n\
Please be informed that the order of \n\
numbers is taken into consideration. \n\
In other words, if your guess(es) match\n\
certain winning numbers, this does not \n\
mean that your particular number(s) consecutively\n\
conform(s) to the winning value(s) as required.\
\n\n\n\n\
Thank you for your patronage. \n\n\
\nIf you wish to try again,\n\
You must wait twenty-four (24)\n\
hours before your next attempt.\n\n\n\
\nThank you for your understanding.', '\
\n\n\n\n')

PAID = False
PRIZE_AWARDED = False

print('\nEnd Time:', game_functions.clean_time())



'''with open('lottery_records.csv', 'w', newline='') as records:
    recording = csv.writer(records)
    recording.writerow(['PLAYER NAME', 'PAID SESSION FEE', \
                  'TIME', \
                  'PLAYER EMAIL', 'WIN', 'CONSENT', 'CODE'\
                  , 'PRIZE AWARDED', 'WINNING NUMBERS', \
                  'PLAYER NUMBERS'])
    
    recording.writerow([PLAYER_NAME, PAID, \
                  game_functions.clean_time(), \
                  PLAYER_EMAIL, win, CONSENT, WINNING_CODE\
                  , PRIZE_AWARDED, random_numbers, \
                  player_numbers])
    records.close()'''

with open('lottery_records.csv', 'a', newline='') as records:
    recording = csv.writer(records)
    '''recording.writerow(['PLAYER NAME', 'PAID SESSION FEE', \
                  'TIME', \
                  'PLAYER EMAIL', 'WIN', 'CONSENT', 'CODE'\
                  , 'PRIZE AWARDED', 'WINNING NUMBERS', \
                  'PLAYER NUMBERS'])'''
    
    
    recording.writerow([PLAYER_NAME, PAID, \
                  game_functions.clean_time(), \
                  PLAYER_EMAIL, win, CONSENT, WINNING_CODE\
                  , PRIZE_AWARDED, random_numbers, \
                  player_numbers])
    records.close()


print('\n\nQuitting in thirty (30) seconds.\n')
for n in range(30):
    
    time.sleep(1)
    if n % 5 == 0 and n != 0:
        print(30 - n, 'Seconds Remaining')

print('\n\n\n\nGoodbye.')
time.sleep(1.2)
