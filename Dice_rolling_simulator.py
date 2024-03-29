#import random
#define a function to roll the dice
#create a dictionary that will have the drawings of the dice
import random
dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }
def roll_dice():
    roll=input("Roll dice (Yes) or (No)? : ")
    while roll.lower()=="yes":
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)

        print("Dice rolled : {} and {}".format(dice1,dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        roll = input("Roll dice again (Yes) or (No)? : ")
roll_dice()