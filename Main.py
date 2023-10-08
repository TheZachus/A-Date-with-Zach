import sys, subprocess, time, os
import GameStuff as g
import Variables as v
import random

#colors
black = "\033[0;30m"
purple = "\033[0;35m"
blue = "\033[0;34m"
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
white = "\033[0;37m"

#ending count

endingCt = v.Count(v.endingsFound)

colorList = [purple, blue, green, red, yellow, white]

#clears the screen according to os
def Clear():
    if os.name == "nt":
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)


#scroll function like in the other game
def Scroll(string, clear=False, anykey=False, txtSpd=v.textSpeed, color=white):
    if clear == True:
        Clear()
    
    print(color, end="")

    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if (letter == '!') or (letter == '.') or (letter == ',') or (letter == '?') or (letter == ':'):
            time.sleep(txtSpd+.25)
        else:
            time.sleep(txtSpd)
    print()

    if anykey == True:
        print("Press any key to continue...")
        input()

#THIS IS WHERE YOU LEFT OFF

def IntroColor(text):
    for letter in text:
        print(random.choice(colorList), end="")
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\t")


def ChangeSpeed():
    Scroll("Type your preferred text scroll speed: ", clear=True)
    print("(F)AST")
    print("(M)EDIUM (default)")
    print("(S)LOW")
    print("(I)NSTANT")

    inp = input().lower()

    if inp == 'f' or 'fast' in inp:
        return 0.001
    elif inp == 'm' or 'medium' in inp:
        return 0.02
    elif inp == 's' or 'slow' in inp:
        return .07
    elif inp == 'i' or 'instant' in inp:
        return 0
    else:
        return v.textSpeed
def MainMenu():
    while True:
        Clear()
        print(white)
        print("(S)TART")
        print("(O)PTIONS")
        if v.endingsFound != []:
            print("(E)NDINGS")
        print("(Q)UIT")
        
        print(black)
        inp = input("Please type an option: ").lower()

        if ("start" in inp) or (inp == "s"):
            return "start"
        elif ("option" in inp) or (inp == 'o'):
            while True:
                Clear()
                print(white)
                print("(T)EXT OPTIONS")
                print("(S)KIP INTRO")
                print("(B)ACK TO MENU")
                
                inp = input("Please type an option: ").lower()

                if inp == "b" or "back" in inp:
                    break
                elif inp == "t" or "text" in inp:
                    v.textSpeed = ChangeSpeed()
                elif inp == 's' or 'skip' in inp:
                    if v.skipIntro == True:
                        v.skipIntro = False
                        Scroll("You will no longer be skipping the intro.", anykey=True, txtSpd=0)
                    else:
                        v.skipIntro = True
                        Scroll("You will now be skipping the intro.", anykey=True, txtSpd=0)
                else: Scroll("That is not a valid option. try again.", anykey=True, txtSpd=0)
        elif ("quit" in inp) or (inp == "q"):
            return " "
        elif ("ending" in inp) or (inp == 'e'):
            Clear()
            print(white)
            for ending in v.endingsFound:
                print(ending)
            print("\nThere are " + str(v.endingsListCt) + " endings to collect total.")
            Scroll('Press any key to return to menu.', color=black)
            input()
        else:
            print("That is not a valid option. try again.")
            input()

def Response(list):
    
    while True:
        Clear()
        num = 0
        for option in list:
            print(yellow)
            num = num + 1
            print(str(num)+". "+option)
        print(black)
        try:
            inp = input("Please type an option: ").lower()
            if ("menu" in inp) or (inp == "m"):
                return Main()
            else:
                inp = int(inp)
        except ValueError:
            Scroll("Not a valid response. Please try again.", anykey=True)
            continue
        return inp

        

def Main():
    Scroll("Welcome to... ", clear=True)
    IntroColor("             _____        _        __          ___ _   _       ______          _     ")
    IntroColor("     /\     |  __ \      | |       \ \        / (_) | | |     |___  /         | |    ")
    IntroColor("    /  \    | |  | | __ _| |_ ___   \ \  /\  / / _| |_| |__      / / __ _  ___| |__  ")
    IntroColor("   / /\ \   | |  | |/ _` | __/ _ \   \ \/  \/ / | | __| '_ \    / / / _` |/ __| '_ \ ")
    IntroColor("  / ____ \  | |__| | (_| | ||  __/    \  /\  /  | | |_| | | |  / /_| (_| | (__| | | |")
    IntroColor(" /_/    \_\ |_____/ \__,_|\__\___|     \/  \/   |_|\__|_| |_| /_____\__,_|\___|_| |_|")
    print()
    print(white)
    input("Press any key to start.")
    while True:

        start = MainMenu()
        if start == "start":
            g.PlayGame()
        else:
            print("You have quit the game.")
            break
if __name__ == "__main__":
    Main()