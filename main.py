from random import *
import sys

def choose_user():
    player = None
    while player not in ["pierre","papier","ciseaux"]:
        player = input("🪨  (pierre)\n📄 (papier)\n✂️  (ciseaux) \n\nVotre choix : ").replace(" ","").lower()
    return(player)

def choose_computer():
    n = randint(1,3)
    if n == 1:
        comp = "pierre"
    elif n == 2:
        comp = "papier"
    else:
        comp = "ciseaux"
    return comp

def play_game(u, c):
    colors = {'red': '\x1b[31m', 'green': '\x1b[32m', 'yellow': '\x1b[33m', 'blue': '\x1b[34m'}
    reset = '\x1b[0m'
    sys.stdout.write(colors.get('yellow') + "\n==========| RESULTAT |==========\n" + reset + "\n")
    if (u == "pierre" and c == "ciseaux") or (u == "papier" and c == "pierre") or (u == "ciseaux" and c == "papier"):
        print(f"Choix Ordianteur : {c}\nChoix Joueur : {u}\n")
        sys.stdout.write(colors.get('green') + "Vous avez gagne." + reset + "\n")
    elif (u == "pierre" and c == "papier") or (u == "papier" and c == "ciseaux") or (u == "ciseaux" and c == "pierre"):
        print(f"Choix Ordianteur : {c}\nChoix Joueur : {u}\n")
        sys.stdout.write(colors.get('red') + "Vous avez perdu." + reset + "\n")
    elif u==c:
        print(f"Choix Ordianteur : {c}\nChoix Joueur : {u}\n")
        sys.stdout.write(colors.get('blue') + "Egalite." + reset + "\n")


print("By 0xtheghost")
play_game(choose_user(), choose_computer())