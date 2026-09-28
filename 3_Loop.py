import random
  
secret = random.randint(1, 10)
attempts = 0

while attempts < 3:
    guess = int(input("Guess a number (1 to 10): "))
    attempts += 1 

    if guess == secret: 
        print("Correct!!!")
        break
    elif guess > secret:
        print("Too High")
    else:
        print("Too Low")
if attempts == 3 and guess != secret:
    print("You lost the number was", secret)
