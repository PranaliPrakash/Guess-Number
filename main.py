

from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def check_guess(level,num):
  ''' The function takes level and num arguments. 
      According to the level sets the attempt counter
      takes(input) a guess(number) from user till the attempts don't equalize to zero(0) or the user guess is correct
      compares guess and the actual number and returns the result accordingly'''

  if level=="easy":
    counter=10
  elif level=="hard" :
    counter=5

  while counter>0 :
    guess= int(input("Make a guess:"))

    if guess==num:
      print(f"You got it! The answer was {num}.")
      counter=0
      return " you win"
    elif guess > num:
      print("Too high \n Guess again")
      counter-=1
      print(f"You have {counter} attempts remaining to guess the number.")  
    elif guess < num:
      print("Too low \n Guess again")  
      counter-=1
      print(f"You have {counter} attempts remaining to guess the number.") 
  print(f"you run out of guesses and the number was {number}")     



import random
number = random.randint(1,100)
#print(number)


choice="yes"
while choice=="yes":
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level=="easy":
    print("You have 10 attempts remaining to guess the number.")
    check_guess(level,number)

  if level=="hard":
    print("You have 5 attempts remaining to guess the number.")
    check_guess(level,number)

  if input("Do you want to play again type yes or no : ") =="no":
    choice="no"
    print("Thankyou for playing!!!!!!")

  
