import random as rand
import Main as m
import time
textSpeed = 0.02
skipIntro = False
endingsList = ["The Perfect Day Ending: I'm glad I spent it with you.",
                "Movie Girl Ending: The things I do for love...",
               "DogFight Ending: We've gotten through ruff-er times, that's for sure!",
               "Murder Mystery Ending: The real murder mystery were the friends we made along the way!",
               "Escape the Chef Ending: Next time, just pay the damn bill!"]
endingsFound = []

dog = {"name": "Dog",
       "hp": 80,
       "dmg": rand.randrange(20,36),
       "heal": rand.randrange(1,11),
       'weap': 'tail'}

chef = {"name": "Chef",
        "hp": 1000,
        "dmg": rand.randrange(75,101),
        "heal": rand.randrange(1,11),
        "weap": "meat cleaver"}

player = {'name': "Elizabeth",
          "hp": 100,
          'dmg': rand.randrange(15,26),
          'heal': rand.randrange(15,36),
          'weap': "Karate Fists",
          'inv': []}
movieCt = 0

#FIX THIS

def Count(alist):
    count = 0
    for item in alist:
        count = count+1
    return count

endingsListCt = Count(endingsList)

def Combat(enemy):
    curEnHp = enemy["hp"]
    curPlHP = player['hp']
    playerTurn = True
    dmg = 0
    m.Clear()
    m.Scroll("You are now in combat with "+ enemy['name']+"!", clear=True, anykey=True)
#main combat loop

    while (curEnHp > 0) and (curPlHP > 0):     
        

    #player turn phase

        while (playerTurn == True) and (curEnHp >0) and (curEnHp >0):
            
            m.Clear()
            print("----------------------------------------------------------------")
            print("            "+ enemy['name']+ " HP: " + str(curEnHp)+ "/" +str(enemy['hp']))
            print('----------------------------------------------------------------')
            print("\n"*4)
            print("----------------------------------------------------------------")
            print("            "+ player['name']+ " HP: "+ str(curPlHP)+"/"+str(player['hp']))
            print("----------------------------------------------------------------\n")
            m.Scroll("It is the player's turn.")
            m.Scroll("What will you do?")
            print("--------------------------------------")
            print("|   (A)ttack         (H)eal          |")
            print("|   (U)se Item       (T)alk to Zach  |")
            print("--------------------------------------")
            print(m.black)
            inp = input("Please type an option: ").lower()
            print(m.white)
            m.Clear()
            if inp == 'a' or 'attack' in inp:
                dmg = player["dmg"]
                curEnHp = curEnHp - dmg
                print(player["name"]+" has dealt ", end="")
                print(m.red, end="")
                print(str(dmg), end="")
                print(m.white, end="")
                print(" damage to "+ str(enemy['name'])+" with "+player['weap']+"!")
                m.Scroll("", anykey=True)

                playerTurn = False

            elif inp == 'h' or 'heal' in inp:

                heal = player["heal"]
                curPlHP = curPlHP + heal
                if curPlHP > player["hp"]:
                    curPlHP = player["hp"]
                print(player["name"]+" has healed ", end="")
                print(m.green, end="")
                print(str(heal), end="")
                print(m.white, end="")
                print(" HP!")
                m.Scroll("", anykey=True)

                playerTurn = False

            elif inp == 'u' or ('use' or 'item') in inp:
                if player['inv'] != []:
                    for item in player["inv"]:
                        print(item)
                    inp = input("Type what item you're going to use: ").lower()
                    if inp in player['inv']:
                        if inp == "chef repellent":
                            curEnHp = 0
                            m.Scroll("You have repelled the chef and he shrivels to dust.", clear=True, anykey=True)

                        playerTurn = True

                    else:
                            m.Scroll("You cannot use that item here.", clear=True, anykey=True)

                else:
                    m.Scroll("You don't have any items in your inventory.", clear=True, anykey=True)
            elif inp == 't' or ('talk' or 'zach') in inp:
                m.Scroll('Holy shit babe, that '+enemy['name']+ " looks really strong!", clear=True, anykey=True, color=m.blue)
                m.Scroll("Zach Proceeds to pass out in fear for a brief moment, then gets back up.", clear=True, anykey=True, color=m.blue)
            else:
                m.Scroll("That is not a valid option. Please type something else.", clear=True, anykey=True)
    if curPlHP <= 0:
            return "lose"
    elif curEnHp <= 0:
        return "win"
    else:
        print()
            

             
#enemy turn phase
        while (playerTurn == False) and (curEnHp > 0) and (curEnHp > 0):
            m.Clear()
            print("----------------------------------------------------------------")
            print("            "+ enemy['name']+ " HP: " + str(curEnHp)+ "/" +str(enemy['hp']))
            print('----------------------------------------------------------------')
            print("\n"*4)
            print("----------------------------------------------------------------")
            print("            "+ player['name']+ " HP: "+ str(curPlHP)+"/"+str(player['hp']))
            print("----------------------------------------------------------------\n")
            m.Scroll("It is "+enemy['name']+"'s turn.", anykey=True)
            decision = rand.randrange(1,11)

#heals if decision is less than 3, attacks otherwise
            if decision <= 3:
                heal = enemy["heal"]
                curEnHp = curEnHp + heal
                if curEnHp > enemy["hp"]:
                    curEnHp = enemy["hp"]
                print(enemy["name"]+" has healed ", end="")
                print(m.green, end="")
                print(str(heal), end="")
                print(m.white, end="")
                print(" HP!")
                m.Scroll("", anykey=True)

            else:
                dmg = enemy["dmg"]
                curPlHP = curPlHP - dmg
                print(enemy["name"]+" has dealt ", end="")
                print(m.red, end="")
                print(str(dmg), end="")
                print(m.white, end="")
                print(" damage to "+ player['name']+" with their "+enemy['weap']+"!")
                m.Scroll("", anykey=True)
            
            playerTurn = True


#murder mystery function

def MurderMystery():
    m.Scroll("I knew it was a good idea to accept a miscellenianous invitation from a guy wearing a suit!", color=m.blue, clear=True, anykey=True)
    m.Scroll("You put on your finest dress and meet your man in the car. He's in his nice suit, so you know he means business.", anykey=True, clear=True)
    m.Scroll("Your chauffeur takes you to the largest mansion at the top of the hill: The Habsburg Estate.", anykey=True, clear=True)
    m.Scroll("You don't know much about the Habsburgs, but you have seen the headlines in the papers that the heir of their fortune is a complete ass.", anykey=True, clear=True)
    m.Scroll("Still, you gotta admit, it is an incredible looking house.", anykey=True, clear=True)
    m.Scroll("You walk in and see not only a crystal chandelier and a massive ice sculpture, but a understated man in a stained, white T-shirt among a slew of other fancially dressed guests.", anykey=True, clear=True)
    m.Scroll("Sup guys. Uh... Glad ya made it.", anykey=True, clear=True, color=m.green)
    m.Scroll("Strike up a conversation with the guests. Or don't. Uh... You can also wait for the special surprise at the end of the night.", anykey=True, clear=True, color=m.green)
    m.Scroll("Or whatever. Just make yourselves comfy, man.", anykey=True, clear=True, color=m.green)
    m.Scroll("Zach instantly moves to the snack table, leaving you in the middle of the ballroom. Such a romantic.", clear=True, anykey=True)

    wait = False
    guests = ["The Host","The Butler","Churchill", "Melanie", "Zach"]
    response = ["What is your relation to the host?",
                "How come you chose to attend?",
                "How do you feel about the host?",
                "Goodbye."]

    responseH = ["How come you threw this party?",
                 "Do you know all these people?",
                 "You seem depressed.",
                 "Goodbye."]

    while wait == False:
        m.Clear()
        print("What will you do at the party?")
        print("------------------------------------------")
        print("|  (M)ingle       (W)ait for Surprise    |")
        print("------------------------------------------")

        print(m.black)
        inp = input("Please type an option: ").lower()
        print(m.white)

        if inp == "m" or "mingle" in inp:
            print("Who will you mingle with?")
            for guest in guests:
                if guest == "Zach":
                    print(m.blue, end="")
                if guest == "Churchill":
                    print(m.red, end="")
                if guest == "Melanie":
                    print(m.purple, end="")
                if guest == "The Host":
                    print(m.green, end="")
                if guest == "The Butler":
                    print(m.white, end="")
                print(guest)

            print(m.black)
            mInp = input("Please type an option: ").lower()
            if "zach" in mInp:
                m.Scroll("NOM NOM NOM NOM NOM NOM NOM NOM NOM NOM NOM NOM", clear=True, anykey=True, color=m.blue)
                m.Scroll("He seems a little busy at the moment...", clear=True, anykey=True)
            elif "mel" in mInp:
                m.Scroll("Oh!!! How delightful, a new guest! And a gorgeous one at that!", clear=True,anykey=True,color=m.purple)
                goodbye  = False
                while goodbye == False:
                    responseRet = m.Response(response)

                    if responseRet == 1:
                        m.Scroll("I'm a family friend of the Hapsburgs. The host's mother and I were roommates in college.",clear=True,anykey=True, color=m.purple)
                        m.Scroll("I've known the host since he was just a little baby!",clear=True,anykey=True, color=m.purple)
                    elif responseRet == 2:
                        m.Scroll("I was quite close friends with the host's mother. Since she's past, I... I don't know what to do with myself.",clear=True,anykey=True, color=m.purple)
                        m.Scroll("I simply chose to attend in her memory.",clear=True,anykey=True, color=m.purple)
                    elif responseRet == 3:
                        m.Scroll("He reminds me of his mother a ton, but he's simply a disgrace to her legacy... I mean the Hapsburgs.",clear=True,anykey=True, color=m.purple)
                        m.Scroll("This little display with the ice sculpture. Tsk! Shirlene would have never allowed that.",clear=True,anykey=True, color=m.purple)
                        m.Scroll("A vein bulges on her forehead. She takes a deep breath.",clear=True,anykey=True)
                        m.Scroll("I apologize. I just can't stand disrespect to legacy.",clear=True,anykey=True, color=m.purple)
                    elif responseRet == 4:
                        goodbye = True
                        m.Scroll("Goodbye, dear! Enjoy the party!", clear=True, anykey=True, color=m.purple)
                    else:
                        m.Scroll("That is not an option. Please pick something else.", clear=True, anykey=True)
            elif "host" in mInp:
                m.Scroll("Sup.", clear=True,anykey=True,color=m.green)
                goodbye  = False
                while goodbye == False:
                    responseRet = m.Response(responseH)

                    if responseRet == 1:
                        m.Scroll("Well, Uh... I bought a massive ice sculpture of myself, and I didn't want it to melt before people could see it.", clear=True,anykey=True,color=m.green)
                        m.Scroll("Guess that's a little selfish, isn't it?", clear=True,anykey=True,color=m.green)
                    elif responseRet == 2:
                        m.Scroll("Not, uh, really, but my parents did before the crash, so I figured they would come.", clear=True,anykey=True,color=m.green)
                        m.Scroll("I don't really have many friends of my own. Uh... A lot of people just like to use me for money.", clear=True,anykey=True,color=m.green)
                        m.Scroll("Sometimes I think that's all I'm good for.", clear=True,anykey=True,color=m.green)
                    elif responseRet == 3:
                        m.Scroll("Yeah, it's been rough since my parents have been gone.", clear=True,anykey=True,color=m.green)
                        m.Scroll("A lot of people like to think I'd act like my parents and be philanthropic rich people like they were.", clear=True,anykey=True,color=m.green)
                        m.Scroll("Uh, Well...", clear=True,anykey=True,color=m.green)
                        m.Scroll("He looks up to the ice sculpture of himself with a spear and shield in hand.", clear=True,anykey=True)
                        m.Scroll("I'm not.", clear=True,anykey=True,color=m.green)
                    elif responseRet == 4:
                        goodbye = True
                        m.Scroll("Later.", clear=True, anykey=True, color=m.purple)
                    else:
                        m.Scroll("That is not an option. Please pick something else.", clear=True, anykey=True)
            elif "churchill" in mInp:
                m.Scroll("Let's make this quick, I have an important phone call in an hour.", clear=True,anykey=True,color=m.red)
                goodbye  = False
                while goodbye == False:
                    responseRet = m.Response(response)

                    if responseRet == 1:
                        m.Scroll("I'm the manager of the late Habsburg estate, now I work for the host.", clear=True, anykey=True, color=m.red)
                    elif responseRet == 2:
                        m.Scroll("I wanted to see how the Habsburg's child was spending his money these days.", clear=True, anykey=True, color=m.red)
                        m.Scroll("He took the crash hard, but it makes sense for him as a Hapsburg to get back on his feet.", clear=True, anykey=True, color=m.red)
                        m.Scroll("How the mighty have fallen.", clear=True, anykey=True, color=m.red)
                    elif responseRet == 3:
                        m.Scroll("Let's just say I'm not impressed.", clear=True, anykey=True, color=m.red)
                        m.Scroll("His mother and father would always try to make the best decisions with their money.", clear=True, anykey=True, color=m.red)
                        m.Scroll("I used to be proud to call them boss. Now it's just embarassing.", clear=True, anykey=True, color=m.red)
                        m.Scroll("Somebody needs to straighten that kid out quick, or there will be hell to pay.", clear=True, anykey=True, color=m.red)
                    elif responseRet == 4:
                        goodbye = True
                        m.Scroll(". . .", clear=True, anykey=True, color=m.purple)
                    else:
                        m.Scroll("That is not an option. Please pick something else.", clear=True, anykey=True)
            
            elif "butler" in mInp:
                m.Scroll("M-MURDER! I mean, uh, hello.", clear=True,anykey=True)
                goodbye  = False
                while goodbye == False:
                    responseRet = m.Response(response)

                    if responseRet == 1:
                        m.Scroll("I'm the host's murderer-- I MEAN Butler. Yes, Butler.",clear=True, anykey=True)
                    elif responseRet == 2:
                        m.Scroll("I'm working him-- I work here! Isn't it obvious that I work here?! Heheh.",clear=True, anykey=True)
                        m.Scroll("The tuxedo, the tray in my hand, I'm his Butler! Hahahaha!",clear=True, anykey=True)
                        m.Scroll("You believe me, right?",clear=True, anykey=True)
                    elif responseRet == 3:
                        m.Scroll("He makes me want to start a fight-- No! He's a delight! That's what I meant!",clear=True, anykey=True)
                        m.Scroll("Yes yes... A truly delightful boy...",clear=True, anykey=True)
                    elif responseRet == 4:
                        goodbye = True
                        m.Scroll("I'll kill you if you don't visit again! Hahaha! I'm joking.", clear=True, anykey=True, color=m.purple)
                    else:
                        m.Scroll("That is not an option. Please pick something else.", clear=True, anykey=True)
            else:
                m.Scroll("That is not a valid option. Try again.", clear=True, anykey=True)


        elif inp == "w" or "wait" in inp:
            wait = True
        else:
            m.Scroll("That is not a valid option. Please type something else.", clear=True, anykey=True)

    m.Scroll("An hour passes, all the while you mingle with the guests and watch your man munch on food.",clear=True,anykey=True)
    m.Scroll("The host stands underneath the ice sculpture with a wineglass, and tings it with a fork.",clear=True,anykey=True)
    m.Scroll("Thank you all for, uh, waiting.",clear=True,anykey=True, color=m.green)
    m.Scroll("I would like to announce my next financial endeavor...",clear=True,anykey=True, color=m.green)
    m.Scroll("A new--",clear=True, color=m.green)
    m.Scroll("All of a sudden, the lights go out. Women scream, babies cry, and Zach faints.",clear=True,anykey=True)
    m.Scroll("There are sounds of a struggle in the darkness, and when the lights flick on, the host is on the floor.",clear=True,anykey=True)
    m.Scroll("There's a hole in his chest pooling blood, and his body is soaking wet.",clear=True,anykey=True)
    m.Scroll("It's then that you notice the spear is missing from the ice sculpture.",clear=True, anykey=True)
    m.Scroll("Zach gets back up and grabs you by the shoulders.",clear=True,anykey=True)
    m.Scroll("Holy shit babe, he's DEAD!",clear=True,anykey=True, color=m.blue)
    m.Scroll("IT WAS YOU! I SAW YOU MOVE IN THE DARKNESS WITH YOUR FOOD! LOOK AT THE TRAIL OF FOOD YOU LEFT BEHIND!",clear=True,anykey=True, color=m.purple)
    m.Scroll("There is a length trail of food leading from the snack table to the host's corpse.",clear=True,anykey=True)
    m.Scroll("WHAT?! No, you gotta believe me! I didn't do it!",clear=True,anykey=True, color=m.blue)
    m.Scroll("No one seems convinced.",clear=True,anykey=True)
    m.Scroll("Quick, they'll trust you, babe! we need your amazing detective skills to figure out who killed him!",clear=True,anykey=True, color=m.blue)
    m.Scroll("I can't go to prison again... I mean I can't go to prison!",clear=True,anykey=True, color=m.blue)

    guests.remove("The Host")

    while True:
        print(m.white)
        print("Who killed the host?")
        for guest in guests:
                if guest == "Zach":
                    print(m.blue, end="")
                if guest == "Churchill":
                    print(m.red, end="")
                if guest == "Melanie":
                    print(m.purple, end="")
                if guest == "The Host":
                    print(m.green, end="")
                print(guest)
        print(m.black)
        kilInp = input("Please type an option: ").lower()
        if "melanie" in kilInp:
            return "win"
        else:
            return "lose"
    



#functions for escape room
    
def GetItem(item):
    if item not in player["inv"]:
        player["inv"].append(item)
        m.Scroll(str(item).upper()+" has been added to your inventory.", anykey=True)

def AddExamOrInt (alist, added):
    if added not in alist:
        for item in added:
            list(alist).append(item)

def UseItem(item, remove=True):
    m.Scroll("This object requires you use an item.")
    m.Scroll("What item would you like to use?")
    for items in player["inv"]:
        print(items)
    print(m.black)
    inp = input("Please type an option: ").lower()
    print(m.white)

    if inp in player["inv"]:
        if inp == item:
            if remove == True:
                player['inv'].remove(item)
            return True
        else:
            m.Scroll("You cannot use this item here.", clear=True, anykey=True)
            return False
    else:
        m.Scroll("This item isn't in your inventory.", clear=True, anykey=True)
        return False
    


def EscapeRoom():

#Intro

    m.Scroll("The chef snickers to himself softly.", clear=True, anykey=True)
    m.Scroll("I WAS HOPING THAT YOU'D SAY THAT!!!!", clear=True, anykey=True, color=m.red)
    m.Scroll("He takes a potato burlap sack out of his back pocket and snatches both you and your man.", clear=True)
    m.Scroll("You don't mind being close to him, but given the circumstances, you both start to panic.",anykey=True)
    m.Scroll("When the bag next opens, the chef has dumped you into his expansive meat locker adorned with human bodies.", clear=True)
    m.Scroll("You wonder if you ate any human with your meal earlier.", anykey=True)
    m.Scroll("YOU TWO DON'T GO ANYWHERE. I'LL BE BACK IN FIVE MINUTES TO SERVE YOU AS FRESH MEAT!", clear=True, anykey=True, color=m.red)
    m.Scroll("There's gotta be something that will help you out of pickle...", clear=True, anykey=True)
    m.Scroll("You have 5 MINUTES to find it!", clear=True, anykey=True)

    timer = time.time()
    examine = ["room","meat", "poster", "lockbox", "mouth"]
    interact = ["lockbox", "meat", 'mouth', "poster"]

    while (time.time()-timer) <= 300 and "chef repellent" not in player["inv"]:
        inp = ""
        m.Clear()
        print(m.white)
        print("You have "+str(round((300-(time.time()-timer))/60,1))+ " minutes to escape!")
        print("--------------------------------------")
        print("|   (E)xamine        (I)nteract      |")
        print("|         (T)alk to Zach             |")
        print("--------------------------------------")
        print(m.black)
        inp = input("Please type an option: ").lower()
        print(m.white)
        m.Clear()

# this is the examine function of all the things in the room.

        if inp == "e" or "examine" in inp:
            m.Scroll("What would you like to examine?")
            for item in examine:
                print(item)
            print(m.black)
            exInp = input("Please type an option: ").lower()
            print(m.white)

            
            if "room" in exInp:
                m.Scroll("You see a few things that catch your attention: a poster, a lockbox, and a large slab of meat and a mouth with crooked teeth.", anykey=True)
            
            elif "poster" in exInp:
                m.Scroll("There are series of symbols on the poster: a pair of identical twins, the letter 'T', and the word 'Free.'",clear=True, anykey=True)
            elif "mouth" in exInp:
                m.Scroll("The mouth is breathing heavily, almost like it's waiting for you to say something...", clear=True, anykey=True)
            elif "lock" or "box" in exInp:
                m.Scroll("There seems to be a spot where you can enter a 2 digit code on top of the lockbox.", clear=True, anykey=True)
            else:
                m.Scroll("You can't examine that.", clear=True, anykey=True)

# interacting function

        elif inp == "i" or "inter" in inp:
            m.Scroll("What would you like to interact with?")
            for item in interact:
                print(item)
            print(m.black)
            intInp = input("Please type an option: ").lower()
            print(m.white)

            if ("lock" or "box") in intInp:
                try:
                    inpLockbox = int(input('ENTER CODE: '))
                    if inpLockbox == 23:
                        m.Scroll("The box opens up. inside is a small key with a square head.", clear=True)
                        GetItem("square key")
                        interact.remove("lockbox")
                        
                    else:
                        m.Scroll('INCORRECT CODE.')
                except ValueError:
                    m.Scroll("There are no letters or spaces on this lock.", clear=True, anykey=True)
            
            if "meat" in intInp:
                key = UseItem("square key")
                if key == True:
                    m.Scroll("A compartment opens up and inside is a UV Flashlight.")
                    GetItem("uv light")
                    interact.remove("meat")
                else:
                    print()

            if "poster" in intInp:
                light = UseItem("uv light", remove=False)
                if light == True:
                    m.Scroll("The UV Light highlights letters that spell two words: DEAD MEAT.", clear=True, anykey=True)

            if "mouth" in intInp:
                mouthinp = input("Say something to the mouth: ").lower()
                if "dead" and "meat" in mouthinp:
                    m.Scroll("The mouth spits up a spray can of something. It reads on the can 'Chef Repellent.' This item can be used in combat.",clear=True, anykey=True)
                    GetItem("chef repellent")
                else:
                    m.Scroll("The mouth does nothing.",clear=True, anykey=True)


        elif inp == "t" or ("zach" or "talk") in inp:
            m.Scroll("Gee, I sure hope that the chef doesn't kill us!", clear=True, anykey=True, color=m.blue)
            m.Scroll("Zach Proceeds to pass out in fear for a brief moment, then gets back up.", clear=True, anykey=True, color=m.blue)
        else:
            m.Scroll("That is not a valid option. Please type something else.", clear=True, anykey=True)