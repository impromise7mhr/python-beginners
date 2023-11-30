import random


def guess():
  range1 = int(input("Enter a 1st range: "))
  range2 = int(input("Enter a 2nd range: "))

  reservedNum = random.randint(range1, range2)

  life = 5
  while life > 0:
    guess = int(input("Guess the number: "))
    if guess < reservedNum:
      print("Too low")
    elif guess == reservedNum:
      print("Congratulations!!! You have Won.")
      break
    else:
      print("Too High")
    life -= 1

  if (life == 0):
    print("You lost. The number was: ", reservedNum)
    print("Better Luck Next Time!!!")

  question = input("Do you want to Continue(Y/N): ")
  game = question.lower()

  return game


a = guess()
if (a == "y"):
  guess()
else:
  print("Thank you for playing. See You Soon!!!")
