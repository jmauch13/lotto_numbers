import random

print("\n")
print("|            ___ |         ")
print("|     |   | |    | / \   / ")
print("|____ |___| |___ | \  \ /  ")
print("                       /   ")
print("                      /    ")
print("|      ___    |     |    ___ ")
print("|     |   | --|-- --|-- |   |")
print("|____ |___|   |     |   |___|")
print("\n")



# National Games
def powerball():
    power_nums = random.sample(range(1, 69), 5)
    power_nums.sort()
    bonus_nums = random.sample(range(1, 26), 1)
    print("Here are your main Powerball numbers:")
    print(power_nums)
    print("Bonus number:",bonus_nums)
    print("Good luck!!")


def mega_millions():
    mega_nums = random.sample(range(1, 70), 5)
    mega_nums.sort()
    mega_bonus = random.sample(range(1, 25), 1)
    print("Here are your main Mega Millions numbers:")
    print(mega_nums)
    print("Bonus number:",mega_bonus)
    print("Good luck!!")

# Ohio Games
def rolling_cash():
    rolling_cash = random.sample(range(1, 49), 6)
    rolling_cash.sort()
    print(rolling_cash)
    print("Good luck!!")

def lucky4_life():
    lucky_nums = random.sample(range(1, 48), 5)
    lucky_nums.sort()
    lucky_bonus = random.sample(range(1, 18), 1)
    print("Here are your main Lucky 4 Life numbers:")
    print(lucky_nums)
    print("Bonus number:",lucky_bonus)
    print("Good luck!!")

def classic_lotto():
    classic_nums = random.sample(range(1, 49), 6)
    classic_nums.sort()
    print(classic_nums)
    print("Good luck!!")

# Pennsylvania & New York
def cash4_life():
    cash_nums = random.sample(range(1, 60), 5)
    cash_nums.sort()
    cash_bonus = random.sample(range(1, 4), 1)
    print("Here are you main Cash 4 Life numbers:")
    print(cash_nums)
    print("Bonus number:",cash_bonus)
    print("Good luck!!")

# Pennsylvania Games
def match6():
    match6_nums = random.sample(range(1, 49), 6)
    match6_nums.sort()
    print(match6_nums)
    print("Good luck!!")

def treasure_hunt():
    treasure_nums = random.sample(range(1, 30), 5)
    treasure_nums.sort()
    print(treasure_nums)
    print("Good luck!!")

# New York Games
def newyork_game():
    newyork_nums = random.sample(range(1, 59), 6)
    newyork_nums.sort()
    print(newyork_nums)
    print("Good luck!!")

def pick10():
    pick10_nums = random.sample(range(1, 80), 10)
    pick10_nums.sort()
    print(pick10_nums)
    print("Good luck!!")


playing = True
while playing:
    user_input = input(
        "\n\n1. National Games \n2. State Games \nPlease select your game type: ")
    if user_input == "1":
        print("\nNational Games is a great choice!")
        national_input = input(
            "\n1. Powerball \n2. Mega Millions \nChoose your game: ")
        if national_input == "1":
            powerball()
        elif national_input == "2":
            mega_millions()

    if user_input == "2":
        print("\nLet's pick a State and get started!")
        state_choice = input(
            "\n1. Ohio \n2. Pennsylvania \n3. New York \nWhich state do you live in? ")
        if state_choice == "1":
            ohio_choices = input(
                "\n1. Lucky for Life \n2. Classic Lottery \n3. Rolling Cash 5 \nWhich Ohio game would you like numbers for? ")
            if ohio_choices == "1":
                lucky4_life()
            elif ohio_choices == "2":
                classic_lotto()
            elif ohio_choices == "3":
                rolling_cash()
        elif state_choice == "2":
            pennsylvania_choice = input(
                "\n1. Cash 4 Life \n2. Match 6 \n3. Treasure Hunt \nWhich Pennsylvania game would you like numbers for? ")
            if pennsylvania_choice == "1":
                cash4_life()
            elif pennsylvania_choice == "2":
                match6()
            elif pennsylvania_choice == "3":
                treasure_hunt()
        elif state_choice == "3":
            newyork_choice = input(
                "\n1. Cash 4 Life \n2. New York Lottery \n3. Pick 10 \nWhich New York game would you like numbers for? ")
            if newyork_choice == "1":
                cash4_life()
            elif newyork_choice == "2":
                newyork_game()
            elif newyork_choice == "3":
                pick10()
        else:
            print("Please select your game")

    again = input("Would you like numbers for another game? ")
    if again == "no" or "n":
        print("Goodbye!")
        playing = False
    else:
        print("Let's get more numbers!")


    
    
