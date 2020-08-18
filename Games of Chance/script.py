#Weronika, 17/08/2020

import random

money = 100

#Write your game of chance functions here
#First function:
def coin_flip(guess, bet):
  if (bet < money):    
    num = random.randint(1, 10)
    if (guess == "Heads" or guess == "Tails"):
      print("Welcome to Flip A Coin Game. Your current amount of money is " + str(money) + " and you are betting: " + str(bet)+".")
      print(". Let's play...")

      if (num > 5) :
        coin = "Heads"
      else :
        coin = "Tails"

      print("The fliped coin landed and it is: " + coin + ", your guess was: " + str(guess) + ".")

      if (guess == coin):
        newMoney = money + bet
        print("You won! and your current amount of monies is now: " + str(newMoney) + "!\n")
        return bet
      else :
        newMoney = money - bet
        print("You lost! and your current amount of monies is now: " + str(newMoney) + "!\n")
        return -bet
    else:
      print("You should enter either 'Heads' or 'Tails' to enter the game.\n")
      return 0
  else:
    print("You are trying to bet more than you have! \n")
    return 0

#Second function:
def cho_han(guess, bet) :
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  diceSum = dice1 + dice2
  print("Welcome to Cho-Han Game. Your current amount of money is " + str(money) + " and you are betting: " + str(bet)+".")
  print(". Let's play...")
  if (guess == "Even"):
    if (diceSum % 2 == 0) : 
      newMoney = money + bet
      print("Your guess was " + guess + " and you were right!. You won your bet. Your current amount of money is: " + str(newMoney)+".\n")
      return bet
    else :
      newMoney = money - bet
      print("You lost your bet, your current amount of monies is :" + str(newMoney)+".\n")
      return -bet
  if (guess == "Odd"):
    if (diceSum % 2 != 0) : 
      newMoney = money + bet
      print("Your guess was " + guess + " and you were right!. You won your bet. Your current amount of money is: " + str(newMoney)+".\n")
      return bet
    else :
      newMoney = money - bet
      print("You lost your bet, your current amount of monies is :" + str(newMoney)+".\n")
      return -bet

#third function:
def card_game(bet) :
  card1 = random.randint(1, 13)
  guess = random.randint(1, 13)
  print("Welcome to Card Game. Your current amount of money is " + str(money) + " and you are betting: " + str(bet)+".")
  print("Your card number: " + str(guess) + ".")
  print("My card is: "+ str(card1) + ".")
  if (guess > card1) :
    newMoney = money + bet
    print("Your card is higher so you won!!! Now you have " + str(newMoney) + " monies.\n")
    return bet
  elif (guess < card1) :
    newMoney = money - bet
    print("You lost... Now you have " + str(newMoney) + " monies.\n")
    return -bet
  else:
    print("It's a tie, you didn't win anything but you didn't loose either \n")
    return 0

#forth function - roulette!
def roulette(guess, bet):
  print("Welcome to the roulette game! Your guess is "+str(guess)+ " and your bet is "+ str(bet) +". Let's roll!")
  num = random.randint(1, 13)
  if (guess == "Even"):
    if (num % 2 == 0 & num !=0):
      print("you won")
      newMoney = money + bet
      print("You have now "+ str(newMoney) + " monies.")
      return bet
    else :
      print("you lost")
      newMoney = money - bet
      print("You have now "+ str(newMoney) + " monies.")
      return -bet
  elif (guess == "Odd"):
    if (num % 2 != 0 & num !=0):
      print("you won")
      newMoney = money + bet
      print("You have now "+ str(newMoney) + " monies.")
      return bet
    else :
      print("you lost")
      newMoney = money - bet
      print("You have now "+ str(newMoney) + " monies.")
      return -bet
  elif (type(guess) is int):
    if (guess == num):
      print("you won")
      newMoney = money + bet
      print("You have now "+ str(newMoney) + " monies.")
      return bet*35
    else :
      print("you lost")
      newMoney = money - bet
      print("You have now "+ str(newMoney) + " monies.")
      return -bet
  else :
    print("you supposed to enter a number between 0 and 36 or 'Odd' or'Even' not " + str(guess) +".")


  

#Call your game of chance functions here
money += coin_flip("Heads", 129)
money += cho_han("Even", 20)
money += card_game(10)
money += roulette(5, 10)

