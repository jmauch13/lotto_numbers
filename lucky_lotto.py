import random
print("Welcome to Lucky Lotto!")
user_input = ''
while True:
    user_input = input(
        "\n1. National Games \n2. State Games \nPlease select your game type: ")
    if user_input == "1":
        print("\nNational Games is a great choice!")
        national_input = input(
            "1. Powerball \n2. Mega Millions \nChoose your game: ")
    elif user_input == "2":
        print("\nLet's pick a State and get started!")
        state_choice = input(
            "1. Ohio \n2. Pennsylvania \n3. New York \nWhich state do you live in? ")
    else:
        print("Please choose an option!")
        break

# National Games


def powerball():
    power_nums = random.sample(range(1, 69), 5)
    power_nums.sort()
    bonus_nums = random.sample(range(1, 26), 1)
    print(power_nums + bonus_nums)


def mega_millions():
    mega_nums = random.sample(range(1, 70), 5)
    mega_nums.sort()
    mega_bonus = random.sample(range(1, 25), 1)
    print(mega_nums + mega_bonus)


# Ohio Games
def rolling_cash():
    rolling_cash = random.sample(range(1, 49), 6)
    rolling_cash.sort()
    print(rolling_cash)


def lucky4_life():
    lucky_nums = random.sample(range(1, 48), 5)
    lucky_nums.sort()
    lucky_bonus = random.sample(range(1, 18), 1)
    print(lucky_nums + lucky_bonus)


def classic_lotto():
    classic_nums = random.sample(range(1, 49), 6)
    classic_nums.sort()
    print(classic_nums)

# Pennsylvania & New York


def cash4_life():
    cash_nums = random.sample(range(1, 60), 5)
    cash_nums.sort()
    cash_bonus = random.sample(range(1, 4), 1)
    print(cash_nums + cash_bonus)

# Pennsylvania Games


def match6():
    match6_nums = random.sample(range(1, 49), 6)
    match6_nums.sort()
    print(match6_nums)


def treasure_hunt():
    treasure_nums = random.sample(range(1, 30), 5)
    treasure_nums.sort()
    print(treasure_nums)

# New York Games


def newyork_game():
    newyork_nums = random.sample(range(1, 59), 6)
    newyork_nums.sort()
    print(newyork_nums)


def pick10():
    pick10_nums = random.sample(range(1, 80), 10)
    pick10_nums.sort()
    print(pick10_nums)
