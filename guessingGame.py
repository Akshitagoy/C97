import random
number = random.randint(1, 9)
chances = 0
print("Welcome to number guessing game")
print("Enter a number between 1 and 9")
while chances < 5:
    guess = int(input("Enter your guess:- "))
    if guess == number:
       print("Congratulation YOU WON!!!")
       break
    elif guess > number:
        print("Your guess was too high : Guess a number lower than", guess)
    else:
        print("Your guess was too low : Guess a number higher than", guess)
    chances+=1

    if not chances < 5:
       print("YOU LOSE!! the number is",number)