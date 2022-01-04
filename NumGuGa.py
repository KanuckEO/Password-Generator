def NGG():
    #number_guessing_game
#Kanuck Shah

#importing libraries
    import random
    from time import sleep

#asking the highest and lowest index they can guess
    low = int(input("Enter lowest number to guess - "))
    high = int(input("Enter highest number to guess - "))

#array
    first = ["first", "second", "third", "fourth", "fifth"]
#variables
    second = 0
#tries counter
    tries = 1
#array for highest and lowest index that they can guess
    numbers = [low, high]
#choosing random number between array above
    number = random.randint(low, high)

#printting for style
    print("\n")
    print("************************************")
    print("Welcome to the number guessing game.")
    print("************************************")
    print("\n")
    print("You will have to choose a number between", low ,"and", high ,"in eight tries")
#delay
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print("\n")

    while tries < 8:
        tries += 1
        print("choose your", first[second] ,"number ", end="")
        ans1 = int(input(""))
        second += 1
        print("You have tried to guess", tries, "times.")
        if int(number) > ans1:
            print("\n")
            print("Too low go higher")
        elif int(number) < ans1:
            print("\n")
            print("Too high go lower")
        elif int(number) == ans1:
            print("\n")
            print("Ding Ding Ding")
            print("You are right")
            print("The number was", number)
            break
        if tries >= 8:
            print("\n")
            print("The number was", number)
            print("Too many tries session ended")
            print("Better luck next time :(")