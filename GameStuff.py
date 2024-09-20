import sys, subprocess, time
import Main as m
import Variables as v

#The end function because it got annoying to do otherwise
def TheEnd(x, theEnd =True, unlock=False):
    if theEnd == True:
        m.Scroll("THE END.", color=m.yellow)
    else:
        m.Scroll('GAME OVER.', color=m.red)
    print(m.black)
    input("press any key to return to the main menu.")
    if unlock == True:
        if v.endingsList[x] not in v.endingsFound:
                v.endingsFound.append(v.endingsList[x])

def Intro():
    m.Scroll("You wake up next to the man of your dreams. He's tall, he's handsome, He's Zach.", clear=True, anykey=True)
    m.Scroll('*yawn* Good morning babe, You sleep well?', color=m.blue, clear=True, anykey=True)

    #first option to respond about how they slept.
    response = ["I had a weird dream last night.",
                "I'm bright eyed and bushy tailed!",
                "No. I had a bad dream."]
    #gets response are returns a value
    responseRet = m.Response(response)

    #options for first response
    if responseRet == 1:
        m.Scroll("Oh, what was it about?", clear=True, anykey=True, color=m.blue)

        response = ["I watched two bears give each other a high five.",
                    "I dreamt about a school shooting that is going to occur on August 5th, 2023, at 12:35 PM Mountain Standard Time.", 
                    "I dreamt I went to school naked!"]
        responseRet = m.Response(response)

        if responseRet == 2:
            m.Scroll("That's... Creepily Specific...", anykey=True, clear=True, color=m.blue)
        else:
            m.Scroll("Woah! Sounds like a pretty crazy if you ask me.", anykey=True, clear=True, color=m.blue)
        m.Scroll("In any case, I hope that your dream helped prepare you for the big day we have today.", anykey=True, clear=True, color=m.blue)

    elif responseRet == 2:
        m.Scroll("That's great to hear! Sounds like you're ready for our big day today.", anykey=True, clear=True, color=m.blue)
    else:
        m.Scroll("Oh. Sorry babe.", anykey=True, clear=True, color=m.blue)
        m.Scroll("He embraces you with his large, beefy, vascular arms. He looks at you.", anykey=True, clear=True)
        m.Scroll("Hope that it won't spoil the big day we have today.", anykey=True, clear=True, color=m.blue)

    m.Scroll("And you know what that day is today?!", clear=True, color=m.blue)
    m.Scroll("Our... ANNIVERSARY!", color=m.blue)
    m.Scroll("I have so many things planned for us to do! I just hope that we can get to all of them today.", color=m.blue)
    m.Scroll("I have a few options to start us off:", anykey=True, color=m.blue)

def PlayGame():
    v.movieCt = 0
    if v.skipIntro == False:
        Intro()
    else:
        print(m.black)
        print("Intro has been skipped.")
    m.Scroll("Right now, we can go on a walk in the park or we can just work on stuff to get things done. But we'd be doing it TOGETHER! :D", clear=True, anykey=True, color=m.blue)
    m.Scroll("So, what'll it be?", anykey=True, clear=True, color=m.blue)

#first choice the player has to make.

    response = ['A walk in the park sounds nice.',
                "Let's hold hands while we work!",
                "I want to watch Schindler's List."]
    responseRet = m.Response(response)

    if responseRet == 1:
        m.Scroll("I was hoping you'd say that. I have a lot to get done, but none of it is as fun as walking with you!", anykey=True, clear=True, color=m.blue)
        m.Scroll("You and Zach walk to Liberty Park, looking at all the ducks, the couples walking around you, and the dogs. Oh god, all the dogs!", anykey=True, clear=True)
        m.Scroll("There's this golden doodle with a star-spangled bandana in particular that walks up to you with it's tail wagging. It has no leesh, it has no collar. But is all smiles.", anykey=True, clear=True)

#dog choice

        response = ["Pet it. Pet it good.",
                    'Keep walking.']
        responseRet = m.Response(response)

        if responseRet == 1:
            m.Scroll("You pet the dog and it smiles contented. Zach smiles at you.", clear=True)
            m.Scroll("You and your dogs. Just remember to take your allergy pills! Don't want to spoil the plans we have for tonight.", clear=True, anykey=True, color=m.blue)
        else:
            m.Scroll('You side step the dog as it leans in for attention. It frowns and its eyes turn red.', clear=True, anykey=True)
            m.Scroll('All of a sudden, the dog scales massively in size, growing a body and muscles similar to a human. Zach grows frightened, and hides behind you.', clear=True, anykey=True)
            m.Scroll('YOU DARE NOT PET ME?! PERISH, FOOLISH MORTAL! YOU SHALL PAY FOR THIS INSULT!', clear=True, anykey=True, color=m.red)
            m.Scroll("Luckily for you, you remember everything from your karate classes as a kid in that very moment.", clear=True, anykey=True, color=m.blue)
            dogCombat = v.Combat(v.dog)

#result of dog combat, win or lose
            if dogCombat == "lose":
                m.Scroll("You have Perished at the hands of a buff dog.", clear=True, anykey=True)
                m.Scroll("GAME OVER.", clear=True, txtSpd=.2)
                TheEnd(2, theEnd=False)
            else:
                m.Scroll("The dog reels back in pain, collapsing in a spat of blood.", clear=True, anykey=True)
                m.Scroll("Woah! I didn't know that you could do that!", clear=True, anykey=True, color=m.blue)
                m.Response(["I'm a ninja, don't ya know?"])
                m.Scroll("Yeah, I c-can... I can see that--", anykey=True, clear=True, color=m.blue)
                m.Scroll("At that very moment, Zach collapses onto the floor with fright.", anykey=True, clear=True)
                m.Scroll("It's clear that your man needs your help. You pick him up by his torso, and run him 20 miles to the nearest hospital.", anykey=True, clear=True)
                m.Scroll("After a brief 10 day coma, your love awakes.", anykey=True, clear=True)
                m.Scroll("Well... This surely isn't an anniversary we're going to forget.", anykey=True, clear=True, color=m.blue)
                TheEnd(2, unlock=True)

            return
    elif responseRet == 2:
        m.Scroll("Sounds like a good time to me, park be damned!", anykey=True, clear=True, color=m.blue)
        m.Scroll("Although not glamorous, you and your man respond to emails, write essays, and whatever else college kids do all while holding hands.",clear=True)
        m.Scroll("By the time Zach looks down at his watch, it's already 5 PM.", anykey=True)
        m.Scroll("Oh sweet Jesus! All this work has almost made us late for our plans!", anykey=True, clear=True, color=m.blue)

    else:
        v.movieCt = v.movieCt+1
        m.Scroll("I'm down! I think I got a copy of Schindler's List around here somewhere...", anykey=True, clear=True, color=m.blue)
        m.Scroll("You and your lovely man watch the entirety of Schindler's list. By the time the movie is done, It's around 5 PM.", anykey=True, clear=True)
        m.Scroll("Oh sweet Jesus! That movie almost made us late for our plans!", anykey=True, clear=True, color=m.blue)

    m.Response(["What plans?"])
    m.Scroll("Well, that's a choice for you to make:", clear=True, anykey=True, color=m.blue)
    m.Scroll("We can either go to a fancy restaurant I booked reservations at or we can go to a fancy dinner party!", clear=True, anykey=True, color=m.blue)
    m.Scroll("So what'll it be?", clear=True, anykey=True, color=m.blue)

#second choice the player has to make.

    response = ["I say the fancy restaurant, as long as you're buying.",
                "You know how much I love fancy dinner parties!",
                "I want to watch Schindler's List."]
    responseRet = m.Response(response)


# restaurant choice

    if responseRet == 1:
        m.Scroll("Haha, anything for you shnookums! Now go put on something nice!", anykey=True, clear=True, color=m.blue)
        m.Scroll("You put on your finest dress and meet your man in the car. He's in his nice suit, so you know he means business.", anykey=True, clear=True)
        m.Scroll("Your chauffeur takes you to one of the fanciest restaurants in town: Gourmandise.", anykey=True, clear=True)
        m.Scroll("You two dine like a king and queen, and have a great time while doing it.", anykey=True, clear=True)
        m.Scroll("And so I said, 'that's not a camel, that's my wife!'", anykey=True, clear=True, color=m.blue)
        m.Response(["Haha. That's funny.", "HAHAHHAHAHAHAHAHAAHAHAHAH YOU'RE SOOOOOO FUNNY ZACH!"])
        m.Scroll("Oh, I love your laugh. Speaking of laughs--", anykey=True, clear=True, color=m.blue)

        m.Scroll("All of a sudden, the chef comes out and slaps the bill violently onto the table.", anykey=True, clear=True)
        m.Scroll("WHO'S GONNA PAY FOR ALL THIS SHIT?!?!", anykey=True, clear=True, color=m.red)
        m.Scroll("That would be me! now here's my--", anykey=True, clear=True, color=m.blue)
        m.Scroll("Uh... This is a little embarassing. Think I left my wallet at home.", anykey=True, clear=True, color=m.blue)
        m.Scroll("*whispering* Do you think you could spot me just this one time, babe? I'd pay you back ASAP.", anykey=True, clear=True, color=m.blue)

#choice for the escape room

        response = ["I think I left my wallet at home too.",
                    "Ugh... Fine. Cheapskate."]
        responseRet = m.Response(response)

        if responseRet == 1:
            v.EscapeRoom()
            m.Scroll("TIME'S UP, FRESH MEAT!", clear=True, anykey=True, color=m.red)
            m.Scroll("ARE YA READY TO BECOME MY NEXT MEAL?!", clear=True, anykey=True, color=m.red)

            response = ["Like hell we are!",
                        "*embraces the sweet release of death*"]
            responseRet = m.Response(response)
            if responseRet == 1:
                combat = v.Combat(v.chef)
                if combat == "win":
                    m.Scroll("You and your man exit the meat locker, a little roughed up, but still looking classy in dress and suit. Zach laughs.", clear=True, anykey=True)
                    m.Scroll("Guess you made him MEAT his maker!", clear=True, anykey=True, color=m.blue)
                    m.Response(["..."])
                    m.Scroll("...", clear=True, anykey=True, color=m.blue)
                    m.Scroll("Gimme a break, I almost just got turned into fillet mignon a few minutes ago.", clear=True, anykey=True, color=m.blue)
                    TheEnd(4, unlock=True)
                    return

                else:
                    TheEnd(4, theEnd=False)
                    return
            else:
                m.Scroll("Hope you like being a soupy broth for some rich guy.", clear=True, anykey=True)
                TheEnd(1, theEnd=False)
            return
        elif responseRet == 2:
            m.Scroll("You fork over some cash, the chef snatches it out of your hand, and scurries away with it.")
            m.Scroll("Phew, thank God. He was starting to give me the heebie jeebies. Thanks for the meal babe.", anykey=True, color=m.blue)
            m.Response(["Don't mention it."])
            m.Scroll("Let's head back to the house.", anykey=True, color=m.blue, clear=True)
            m.Scroll("Your 'chauffeur' drives you back to the house, a little defeated, but still valiant.", anykey=True, clear=True)

# murder mystery
    elif responseRet == 2:
        m.Scroll("There's the [player name] I know and love! now go put on something nice, we got a mysterious manor to drive to!", anykey=True, clear=True, color=m.blue)
        myst = v.MurderMystery()
        if myst == "win":
            m.Scroll("The cops burst in. You present your evidence for who you thought did it.",clear=True, anykey=True)
            m.Scroll("They listen. Because you present such a good case, they emphatically agree with you and arrest Melanie on the spot.",clear=True, anykey=True)
            m.Scroll("NO! THAT LITTLE BRAT COULDN'T GET AWAY WITH IT! TAINTING SHIRLENE'S LEGACY LIKE THAT!",clear=True, anykey=True, color=m.purple)
            m.Scroll("SHIRLEEEEEENE!",clear=True, anykey=True, color=m.purple)
            m.Scroll("The cops take her away.",clear=True, anykey=True)
            m.Scroll("You and your man walk away from that night with your heads held high, as the guests liked both of you so much, the left you the Hapsburg fortune.",clear=True, anykey=True)
            m.Scroll("I guess crime does pay after all. SOLVING crimes!",clear=True, anykey=True, color=m.blue)
            m.Response(["..."])
            m.Scroll("... Tough crowd.",clear=True, anykey=True, color=m.blue)
            TheEnd(3, unlock=True)
        else:
            m.Scroll("The cops burst in. You present your evidence for who you thought did it, but it's simply unconvincing.",clear=True, anykey=True)
            m.Scroll("Hope you like long distance from a jail cell.",clear=True, anykey=True)
            TheEnd(3, theEnd=False)
        return
    else:
        v.movieCt = v.movieCt+1
        if v.movieCt != 0:
            m.Scroll("Um... I think that we just watched Schindler's List. Do you really want to watch it again?", anykey=True, clear=True, color=m.blue)
            m.Scroll("You nod emphatically, the desire to watch Schindler's List plain on your face. Zach deeply sighs.", anykey=True, clear=True)
            m.Scroll("Alright... You're lucky you're cute. I'll go put it on again.", anykey=True, clear=True, color=m.blue)
            m.Scroll("You and Zach both watch Schindler's List a second time, but this time, you can see it waning on Zach's face.", clear=True)
            m.Scroll("You haven't even broken a sweat. By the time the movie is done, it's around 10 PM.", anykey=True)
        else:
            m.Scroll("I'm down! I think I got a copy of Schindler's List around here somewhere...", anykey=True, clear=True, color=m.blue)
            m.Scroll("You and your lovely man watch the entirety of Schindler's list. By the time the movie is done, It's around 10 PM.", anykey=True, clear=True)


    m.Scroll("Well... It's getting pretty late. Is there anything else that you're wanting to do today?", anykey=True, clear=True, color=m.blue)


    response = ["Nope, I think I'm about ready for bed.",
                "I want to watch Schindler's List."]
    responseRet = m.Response(response)

    if responseRet == 1:
        m.Scroll("*Yawn* Yep, I'm about ready for bed too. Let's get some shut eye.", anykey=True, clear=True, color=m.blue)
        m.Scroll("In your pijamas, you and Zach settle into the bed that you both woke up in earlier this morning.", clear=True)
        m.Scroll("He wraps his large, vascular arms around you, but he pushes you away so he can see your whole face while he speaks.", clear=True)
        m.Scroll("Hey, thank you for being with me for so long, honey. I know we've had our ups and downs, and this date wasn't perfect by any means...", anykey=True, clear=True, color=m.blue)
        m.Scroll("But it means a lot to me that you actually went with me. And that you've stuck with me this long.", anykey=True, clear=True, color=m.blue)
        m.Scroll("I hope I haven't gotten annoying yet, haha. I know you haven't. Well, sometimes actually. Anyways, I love you very much.", anykey=True, clear=True, color=m.blue)
        m.Response(["I love you very much too, Zach."])
        m.Scroll("Happy anniversary, honey.", anykey=True, clear=True, color=m.blue)
        m.Scroll("He smiles. You fall asleep in each other's arms.", anykey=True, clear=True)
        m.Scroll("Still...", anykey=True, clear=True)
        m.Scroll("You wonder what else could've happened today...", anykey=True, clear=True)

        TheEnd(0, unlock=True)
        return

    elif responseRet == 2:
        if v.movieCt == 1:
            m.Scroll("Um... I think that we just watched Schindler's List. Do you really want to watch it again?", anykey=True, clear=True, color=m.blue)
            m.Scroll("You nod emphatically, the desire to watch Schindler's List plain on your face. Zach deeply sighs.", anykey=True, clear=True)
            m.Scroll("Alright... You're lucky you're cute. I'll go put it on again.", anykey=True, clear=True, color=m.blue)
            m.Scroll("You and Zach both watch Schindler's List a second time, but this time, you can see it waning on Zach's face.", clear=True)
            m.Scroll("You haven't even broken a sweat. By the time the movie is done, Zach has fallen asleep on your shoulder.", anykey=True)
            m.Scroll("Guess he couldn't take how deep it was. Thank God you love him.", anykey=True)

            TheEnd(1)
            return
        
        elif v.movieCt == 2:
            m.Scroll("Okay, I think I've watched enough Schindler's List today.", anykey=True, clear=True, color=m.blue)
            m.Scroll("You beg and cry and scream, claiming that you need to watch it because it's 'deep like our relationship.'", anykey=True, clear=True)
            m.Scroll("Um... I don't think you wanna compare our relationship to a holocaust movie.", anykey=True, clear=True, color=m.blue)
            m.Scroll("But I guess you make a point. I do like seeing how happy that movie makes you...", anykey=True, clear=True, color=m.blue)
            m.Scroll("Ah hell, let's play it.", anykey=True, clear=True, color=m.blue)

            m.Scroll("You and your man sit down to watch Schindler's list for a 3rd time that day, but he doesn't seem nearly as tired.", clear=True)
            m.Scroll("In fact, he seems happy that the movie reminds him of you. About 30 minutes in, he falls asleep on your shoulder.")
            m.Scroll("Guess he couldn't take how 'deep' it was for the 3rd time today. Moron.", anykey=True)

            TheEnd(1, unlock=True)
            return

        else:
            m.Scroll("I'm down! I think I got a copy of Schindler's List around here somewhere...", anykey=True, clear=True, color=m.blue)
            m.Scroll("About 30 minutes in, he falls asleep on your shoulder.")
            m.Scroll("Guess he couldn't take how deep it was. Thank God you love him.", anykey=True)

            TheEnd(1)
            return
