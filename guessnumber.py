import random

print('---------------------------------------')
print('        GUESS THAT NUMBER GAME')
print('---------------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1
name = input('What is your name?')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {}, your number {} was TOO LOW' .format(name, guess))
    elif guess > the_number:
        print('Sorry {}, your number {} was TOO HIGH' .format(name, guess))
    else:
        print('Congratulation {}, you Won!! Your number was {}' .format(name, guess))

print('Done!')


