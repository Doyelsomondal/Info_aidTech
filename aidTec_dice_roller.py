import random

def roll_dice(num_dice):

     dice_rolls =[random.randint(1,6) for _ in range(num_dice)]
                  
     return dice_rolls

def main():
    print("Welcome to the Dice Rolling App!")

    while True:

        num_dice =int(input("enter the number of dice to roll:"))


        dice_results = roll_dice(num_dice)
        print("Dicd rolls:", dice_results)


        play_again= input("Do you want to roll again?(yes/np):").lower()
        if play_again not in['yes','y']:
             print("Thank you for using Dice Rolling App.Goodbye!")
             break


if __name__ =="__main__":
 main()     
    
