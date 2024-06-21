import random
import time

# Dictionary to display dice with stars
stardashDisplay = {
    1: (
        "┌────★────┐",
        "│★        │",
        "│    1★   │",
        "│       ★ │",
        "└──★──────┘"
    ),
    2: (
        "┌──★──────┐",
        "│    ★    │",
        "│★   2    │",
        "│     ★   │",
        "└───────★─┘"
    ),
    3: (
        "┌───────★─┐",
        "│  ★      │",
        "│    3★   │",
        "│★        │",
        "└─────★───┘"
    ),
    4: (
        "┌─────★───┐",
        "│       ★ │",
        "│  ★ 4    │",
        "│    ★    │",
        "└★────────┘"
    ),
    5: (
        "┌★────────┐",
        "│     ★   │",
        "│    5  ★ │",
        "│  ★      │",
        "└────★────┘"
    ),
    6: (
        "┌────★────┐",
        "│★        │",
        "│    6★   │",
        "│       ★ │",
        "└──★──────┘"
    ),
}

def roll_dice(num_of_dice):
    dice = [random.randint(1, 6) for _ in range(num_of_dice)]
    total = sum(dice)
    for line in range(5):
        for star in dice:
            print(stardashDisplay[star][line], end=" ")
        print()
    return total

def player_roll():
    num_of_dice_roll = int(input("Enter the number '6' to roll the 6 dice: "))
    total = roll_dice(num_of_dice_roll)
    print(f"Player's total: {total}")
    return total

def winter_bot_roll():
    print("... Bot rolling")
    time.sleep(0.1)
    total = roll_dice(6)
    print(f"WinterBot's total: {total}")
    return total

def starDice():
    print("-------------------------------------")
    print("★★★★★ STAR DICE ★★★★★")
    print("-------------------------------------")
    player_name = input("Enter your name: ")
    print(f"Great! {player_name}, you roll first!")
    print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")

    player_score = 0
    winter_bot_score = 0

    for _ in range(5):
        player_total = player_roll()
        winter_bot_total = winter_bot_roll()

        if player_total > winter_bot_total:
            print(f"{player_name} rolled {player_total} - You win!")
            player_score += 1
        elif player_total < winter_bot_total:
            print(f"WinterBot rolled {winter_bot_total} - Bot wins!")
            winter_bot_score += 1
        else:
            print("It's a draw!")

    print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
    if player_score > winter_bot_score:
        print(f"{player_name} wins with {player_score} wins!★ & WinterBot loses with a score of {winter_bot_score}.")
    elif player_score < winter_bot_score:
        print(f"WinterBot wins with {winter_bot_score} wins!★ & {player_name} loses with a score of {player_score}.")
    else:
        print(f"It's a tie! {player_name} score: {player_score} & WinterBot score: {winter_bot_score}")

if __name__ == "__main__":
    starDice()

