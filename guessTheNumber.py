import random
import sys

def gameOptions():
    gameOpt = int(input("Enter a game option( Easy(1)/ Medium(2)/ Hard(3)/ RandomGame(4): "))
    
    if gameOpt == 1:
        game1()
    elif gameOpt == 2:
        game2()
    elif gameOpt == 3:
        game3()
    elif gameOpt == 4:
        randomGame()
  
def game1():
    randomNumber = random.randint(1,10)
    guess = 0    
    while randomNumber != guess:
        playerGuess =  int(input(" Enter a number between 1 and 10: "))
        
        if playerGuess == randomNumber:
            print(" You Won!")
            playAgain()
        else:
            print(" Sorry, do you want to try again")
            playAgain()

def game2():
    randomNumber = random.randint(1,50)
    guess = 0    
    while randomNumber != guess:
        playerGuess =  int(input(" Enter a number between 1 and 50: "))
        
        if playerGuess == randomNumber:
            print(" You Won!")
            playAgain()
        else:
            print(" Sorry, do you want to try again")
            playAgain()

def game3():
    randomNumber = random.randint(1,1000)
    guess = 0    
    while randomNumber != guess:
        playerGuess =  int(input(" Enter a number between 1 and 1000: "))
        
        if playerGuess == randomNumber:
            print(" You Won!")
            playAgain()
        else:
            print(" Sorry, do you want to try again")
            playAgain()

def randomGame():
    x = random.randrange(100000)
    a = random.randint(1,x)
    i = int(input("Enter a number between 1 and random number generated by the computer: "))
    if i == a:
        print(" Correct!")
        playAgain()
    else:
        playAgain()
        
def playAgain():
    plyAgainOpt = int(input("What do you want to do next( game 1 -> 1, game 2 -> 2, game 3 -> 3 and exit -> 4): "))
    
    if plyAgainOpt == 1: 
        game1()
    elif plyAgainOpt == 2:
        game2()
    elif plyAgainOpt == 3:
        game3()
    elif plyAgainOpt == 4:
        sys.exit()

gameOptions()