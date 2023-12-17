# Import the random module
import random

#generate a random number between 1 and 100
number = random.randint(1,100)

# Initialize the number of guesses
guesses = 0

# loop until the user guesses correctly or run out of attempts
while guesses < 5:
# Ask the user to enter a guess 
 guess = int(input("enter your guess: "))

# increment the number of guesses 
guesses += 1

# check if the guess is correct
if guess == number :
# print a congratulatory  message
  print("corrrect!")
  print("Congratulation! You guessed the number.")
  # Break out of the loop 
  #break
# check if the guess is too high
elif guess > number:
  #Print a feedback message 
  print("Too high")
  # check if the guess is too low
else:
  # print a feedback message
  print("Too low")
  print("Congratulation! You guessed the number.")
  # Break out of the loop 
  #break
# Check if the guess is too low
# else:
# Print a feedback message 
print("too low")
# Check if the user ran out of guesses
if guesses == 5 and guess != number:
  #print a game over message 
  print("Game over! Yoou ran out of guesses.")
  print("The number was", number)

