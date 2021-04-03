from game_data import data
from art import logo,vs
from random import choice
from os import system

def getRandomData(data):
  statement = choice(data)
  str = f"{statement['name']}, a {statement['description']}, from {statement['country']}"
  return str,statement['follower_count']

def printData(statementA,statementB):
  
  print(logo)
  print('Compare A: '+statementA)
  print(vs)
  print('Against B: '+statementB)

def main():
  score = 0 
  statementB = getRandomData(data) 
  continue_guessing = True

  while continue_guessing:
    statementA = statementB
    while statementA == statementB:
      statementB = getRandomData(data) 

    printData(statementA[0],statementB[0])
    user_guess = input("Which Do You Think has More Follower Count. 'A' or 'B' : ").lower()
    if checkResult(statementA[1],statementB[1],user_guess):
      system('cls')
      score += 1;
      print(f'Correct Guess .Your Score is {score}')
    else:
      continue_guessing = False
  
  print(f"GAME OVER : YOUR FINAL SCORE IS : {score}")
  
def checkResult(first,second,guess):
    if first>second:
      return guess == 'a'
    else:
      return guess == 'b'   


main()
input('Press Enter To Exit')
