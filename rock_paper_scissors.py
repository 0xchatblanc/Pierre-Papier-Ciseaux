from random import *
import sys

def choose_user():
    player = None
    while player not in ["rock", "paper", "scissors"]:
        player = input("🪨 (rock)\n📄 (paper)\n✂️ (scissors) \n\nYour choice: ").replace(" ", "").lower()
    return player

def choose_computer():
    n = randint(1, 3)
    if n == 1:
        comp = "rock"
    elif n == 2:
        comp = "paper"
    else:
        comp = "scissors"
    return comp

def play_game(user, computer):
    colors = {'red': '\x1b[31m', 'green': '\x1b[32m', 'yellow': '\x1b[33m', 'blue': '\x1b[34m'}
    reset = '\x1b[0m'
    sys.stdout.write(colors.get('yellow') + "\n==========| RESULT |==========\n" + reset + "\n")
    if (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        print(f"Computer's choice: {computer}\nYour choice: {user}\n")
        sys.stdout.write(colors.get('green') + "You won!" + reset + "\n")
    elif (user == "rock" and computer == "paper") or (user == "paper" and computer == "scissors") or (user == "scissors" and computer == "rock"):
        print(f"Computer's choice: {computer}\nYour choice: {user}\n")
        sys.stdout.write(colors.get('red') + "You lost." + reset + "\n")
    elif user == computer:
        print(f"Computer's choice: {computer}\nYour choice: {user}\n")
        sys.stdout.write(colors.get('blue') + "It's a tie." + reset + "\n")


print("By 0xchatblanc")
play_game(choose_user(), choose_computer())
