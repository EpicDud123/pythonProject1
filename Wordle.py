import random
number_list = ["strap", "steak", "jewel", "minor", "apple", "touch", "voter", "queue", "blind", "ferry", "chief", "river", "fraud", "marsh", "thumb", "flush", "serve", "color", "crash", "stand"]

# welcoming the user
name = input("What is your name? ")

print("Hello, " + name, "Time to play hangman!")

print("")

# wait for 1 second


print("Start guessing...")
# here we set the secret
word = (random.choice(number_list))


# creates an variable with an empty value
guesses = ''

# determine the number of turns
turns = 6

# Create a while loop

# check if the turns are more than zero
while turns > 0:

    # make a counter that starts with zero
    failed = 0

    # for every character in secret_word
    for char in word:

        # see if the character is in the players guess
        if char in guesses:

            # print then out the character
            print(char, end='')

        else:

            # if not found, print a dash
            print("_", end=''),

            # and increase the failed counter with one
            failed += 1

    print()  # this prints a new line for some space

    # if failed is equal to zero

    # print You Won
    if failed == 0:
        print("wow i can't believe you wasted some time of your life trying to beat this i know you think you won but did you really win you wasted some time of your life so it's hard to say you won. Here's the amount of attemps you have left aswell:" + guesses)

        # exit the script
        break

        # ask the user go guess a character
    guess = input("guess a character:").lower()
    if len(guess) < 5:
        print("H-hey your not supposed to do that")
    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word:

        # turns counter decreases with 1 (now 9)
        turns -= 1

        # print wrong
        print("Wrong")

        # how many turns are left
        print("You have", + turns, 'more guesses')

        # if the turns are equal to zero
        if turns == 0:
            # print "You Lose"
            print("you Lose")
            print("wow your so bad here have the word loser:" + word)
