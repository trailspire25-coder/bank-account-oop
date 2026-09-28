import random # import a random number.
  
secret = random.randint(1, 10) # create one random whole number between 1 and 10 and stores it in secret,
attempts = 5 # stores remaining guesses.

while attempts > 0: # keeps playing while there are attempts left, if 0 attempts remains, loop stops,
    guess = int(input("Guess a number (1 to 10): ")) # ask the user to input a number then stores it in guess.

    if guess == secret: 
        print("Correct!!!")
        break # if the secret number given by the user is equal to the secret number then its correct, then stop.

    elif guess > secret: # and if the guess is greater than secret number,
        attempts -= 1 # subtract one attempt from the total attempts,
        print("Too High") # then print too high.

    else:
        attempts -= 1 # else subtract 1 from attempts then, 
        print("Too Low") # print too low.
        
    if attempts > 0: # if attempts is greater than 0,
        print("Wrong geuss.") # show a wrong guess,
        print("Attemps left:", attempts) # then show attempts left and continue with the loop.

else: # this runs after the while loop is finished, and if the user does not guess the secret number after the all the attempts,
  print("Game Over! You ran out of attempts.") # then show lost,
  print("The number was", secret) # after that show the secret number.