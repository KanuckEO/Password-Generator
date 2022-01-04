import password_maker
import Calculator
import Dice
import divis
import multi
import RPS
import NumGuGa
import time

def intro():
    print("****************************")
    print("Welcome To The Everything!!!")
    print("****************************")

    print("Warning This Tool is Case sensitive so when you type type the way the developer has told you too")
    print("Choose where you would like too go: ")
    print("- Tools (Type 1)")
    print("- Games (Type 2)")
    choose_menu = input("Type here: ")
    print("")

    if choose_menu == "2":
        print("Choose which game you would like to go too")
        print("- Rock Paper Scissors (Type 1)")
        print("- Number Guessing Game (Type 2)")
        choose_game = input("Type here: ")
        print("")

        if choose_game == "2":
            NumGuGa.NGG()
            print("")
            time.sleep(1)
            print("Going Back To Menu Because Program Is Done.")
            time.sleep(1)
            intro()
        elif choose_game == "1":
            RPS.RPS()
            print("")
            time.sleep(1)
            print("Going Back To Menu Because Program Is Done.")
            time.sleep(1)
            intro()
    elif choose_menu == "1":
        print("Choose which Tools you would like to go too")
        print("- Password Maker (Type 1)")
        print("- Calculator (Type 2)")
        print("- Divisibilty checker (Type 3)")
        print("- Multiplication Tables (Type 4)")
        print("- Dice Roller (Type 5)")
        choose_tool = input("Type here: ")
        print("")
        
        if choose_tool == "1":
            password_maker.password_maker()
            print("")
            time.sleep(1)
            print("Going Back To Menu Because Program Is Done.")
            time.sleep(1)
            intro()
        elif choose_tool == "2":
            Calculator.Calculator()
            print("")
            time.sleep(1)
            print("Going Back To Menu Because Program Is Done.")
            time.sleep(1)
            intro()
        elif choose_tool == "3":
            divis.divis()
            print("")
            time.sleep(1)
            print("Going Back To Menu Because Program Is Done.")
            time.sleep(1)
            intro()
        elif choose_tool == "4":
            multi.multi()
            print("")
            time.sleep(1)
            print("Going Back To Menu Because Program Is Done.")
            time.sleep(1)
            intro()
        elif choose_tool == "5":
            Dice.dice()
            print("")
            time.sleep(1)
            print("Going Back To Menu Because Program Is Done.")
            time.sleep(1)
            intro()

intro()

    
    
    