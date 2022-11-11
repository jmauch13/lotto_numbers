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
    print("\nGood luck!!")


def mega_millions():
    mega_nums = random.sample(range(1, 70), 5)
    mega_nums.sort()
    mega_bonus = random.sample(range(1, 25), 1)
    print("Here are your main Mega Millions numbers:")
    print(mega_nums)
    print("Bonus number:",mega_bonus)
    print("\nGood luck!!")

# Ohio Games
def rolling_cash():
    rolling_cash = random.sample(range(1, 49), 6)
    rolling_cash.sort()
    print(rolling_cash)
    print("\nGood luck!!")

def lucky4_life():
    lucky_nums = random.sample(range(1, 48), 5)
    lucky_nums.sort()
    lucky_bonus = random.sample(range(1, 18), 1)
    print("Here are your main Lucky 4 Life numbers:")
    print(lucky_nums)
    print("Bonus number:",lucky_bonus)
    print("\nGood luck!!")

def classic_lotto():
    classic_nums = random.sample(range(1, 49), 6)
    classic_nums.sort()
    print(classic_nums)
    print("\nGood luck!!")

# Pennsylvania & New York
def cash4_life():
    cash_nums = random.sample(range(1, 60), 5)
    cash_nums.sort()
    cash_bonus = random.sample(range(1, 4), 1)
    print("Here are you main Cash 4 Life numbers:")
    print(cash_nums)
    print("Bonus number:",cash_bonus)
    print("\nGood luck!!")

# Pennsylvania Games
def match6():
    match6_nums = random.sample(range(1, 49), 6)
    match6_nums.sort()
    print(match6_nums)
    print("\nGood luck!!")

def treasure_hunt():
    treasure_nums = random.sample(range(1, 30), 5)
    treasure_nums.sort()
    print(treasure_nums)
    print("\nGood luck!!")

# New York Games
def newyork_game():
    newyork_nums = random.sample(range(1, 59), 6)
    newyork_nums.sort()
    print(newyork_nums)
    print("\nGood luck!!")

def pick10():
    pick10_nums = random.sample(range(1, 80), 10)
    pick10_nums.sort()
    print(pick10_nums)
    print("\nGood luck!!")

def main_menu():
    print("\n")
    print("----------------------------------------")
    print("|              Main Menu:              |")
    print("----------------------------------------")
    print("| 1. National Games     2. State Games |")
    print("----------------------------------------")
    print("|               3. Exit                |")
    print("----------------------------------------")
    print("\n")

def national_menu():
    print("\n")
    print("-----------------------------------------")
    print("|            National Games:            |")
    print("-----------------------------------------")
    print("| 1. Powerball         2. Mega Millions |")
    print("-----------------------------------------")
    print("|           3. Main Menu                |")
    print("-----------------------------------------")
    print("\n")

def state_menu():
    print("\n")
    print("-----------------------------------------")
    print("|             State Games:              |")
    print("-----------------------------------------")
    print("| 1. Ohio Games       2. New York Games |")
    print("-----------------------------------------")
    print("| 3. Pennsylvania Games   4. Main Menu  |")
    print("-----------------------------------------")
    print("\n")
    


while True:
    main_menu()
    user_input = input(
        "\nPlease select your game type: ")
    if user_input == "1":
        print("\nNational Games is a great choice!")
        national_menu()
        national_input = input(
            "\nChoose your game: ")
        if national_input == "1":
            powerball()
        elif national_input == "2":
            mega_millions()
        elif national_input == "3":
            main_menu()
    elif user_input == "3":
        print("Goodbye!")
        exit()

    if user_input == "2":
        print("\nLet's pick a State and get started!")
        state_menu()
        state_choice = input(
            "\nWhich state do you live in? ")
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
            newyork_choice = input(
                "\n1. Cash 4 Life \n2. New York Lottery \n3. Pick 10 \nWhich New York game would you like numbers for? ")
            if newyork_choice == "1":
                cash4_life()
            elif newyork_choice == "2":
                newyork_game()
            elif newyork_choice == "3":
                pick10()
        elif state_choice == "3":
            pennsylvania_choice = input(
                "\n1. Cash 4 Life \n2. Match 6 \n3. Treasure Hunt \nWhich Pennsylvania game would you like numbers for? ")
            if pennsylvania_choice == "1":
                cash4_life()
            elif pennsylvania_choice == "2":
                match6()
            elif pennsylvania_choice == "3":
                treasure_hunt()

    


            
                

    
    
