from random import randint
from logos import black_jack

print(black_jack)
start_another = input("Do you want to play BlackJack? yes or no. ")


def display_score():
    print("\nScores are")
    print(f"player : {player} count={sum(player)}")
    print(f"opponent : {computer} count={sum(computer)}")


def decision():
    if 11 in player and sum(player)>21:
        player.remove(11)
        player.append(1)
        next_card = input("Type 'y' to get another card,type 'n' to pass: ")
        if next_card == "y":
            deal_card()

    if 11 in computer and sum(computer)>21:
        computer.remove(11)
        computer.append(1)

    while sum(computer) < sum(player):
        computer.append(randint(2, 11))

    display_score()
    if sum(player) > 21:
        print("\nYou Lost")
    if sum(computer) > 21  and sum(player) <= 21:
        print("\nYou Won!")
    if sum(computer) > sum(player) and sum(computer) <= 21:
        print("\nYou Lost!")
    if sum(computer) == sum(player):
        print("\nDRAW")
    if sum(computer) < sum(player)  and sum(player) <= 21:
        print("\nYou Won!")


def deal_card():
    player.append(randint(2, 11))
    if 11 in player and sum(player)>21:
        player.remove(11)
        player.append(1)
    display_score()
    if sum(player) > 21:
        return
    next_card = input("Type 'y' to get another card,type 'n' to pass: ")
    if next_card == "y":
        deal_card()


while start_another != "no":
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player = [randint(2, 11), randint(2, 11)]
    computer = [randint(2, 11)]
    print(f'Your cards are [{player[0], player[1]}]')
    print(f"Computer's first card {computer[0]}")
    next_card = input("Type 'y' to get another card,type 'n' to pass: ")
    if next_card == "y":
        deal_card()
    decision()
    another = input("Do you want to play BlackJack? yes or no. ")
    if another == "no":
        start_another = "no"
