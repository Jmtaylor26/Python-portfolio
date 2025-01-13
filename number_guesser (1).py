#Jade Taylor

#Initialize
import random

#function
guess = input("guess a number between 1 and 10")
number = print (random.randint(1,10))
if guess==number:
    print("you got it")
else:
    print("you 1 more chance")
    guess2=input("please ender another number between 1-10")
    if number==int(guess2):
        print("you guessed correctly")
    else:
        print("you failed")


#main
