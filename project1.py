#project number 4
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    pleyers = input("Enter the number of pleyer between (2 - 4) : ")
    if pleyers.isdigit():
        pleyers = int(pleyers)
        if 2 <= pleyers <= 4:
            break
        else:
            print("players must be between 2 - 4")
    else:
        print("Invald input try again.")

max_score = 50
player_score = [0 for _ in range(pleyers)]

while max(player_score) < max_score:
    for player_ind in range(pleyers):
        print(" \n player number ", player_ind + 1, "is started to roll")
        print("you score ", player_score[player_ind], "\n")
        current_score = 0
        while True:
            should_roll = input("je undgepensda kucheza jibu  (n)? ")
            if should_roll.lower() != "n":
                break
            value = roll()
            if value == 1:
                print(" 1! is rolled")
                break
            else:
                current_score += value
                print("you rolled ", value)
            print("you score is ", current_score)
        player_score[player_ind] += current_score
        print("You total score is : ", player_score[player_ind])
max_score = max(player_score)
win_index = player_score.index(max_score)
print("mshindi ni mchezaji mwenye number ", win_index + 1, " ameshinda alama ", max_score)