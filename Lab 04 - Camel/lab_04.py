import random


def main():
    print("Welcome to Breath Of the Wild!")
    print("You have been asleep for 100 years Link!")
    print("Get to the castle to slay Ganon and free the princess!")
    done = False
    heart = 3
    stamina = 5
    weapons = 0
    story = 0
    champion_ability = 0
    gale_uses = 3
    grace_uses = 1
    fury_uses = 3
    protection_uses = 3
    while not done:
        master_mode = input("play in master mode? y/n  ")
        if master_mode == "n":
            print("Chicken")
            done = True
        while master_mode == "y":
            print("Ok")
            print("Complete the 4 shrines to leave the great plateau \n ")
            master_mode = input("""Do you 
            A: complete the shrines normally 
            B: speedrun like a boss
            C: Go on a bokoblin killing spree
            D: Kill the master mode Lynel
            E: quit 
            
            - """)
            if master_mode == "A":
                print("You completed the shrines and got all four spirit orbs now what do you do?")
                master_mode = "1"
            elif master_mode == "B":
                success = random.randrange(10)
                if success == 0:
                    print("You survived and faster than ever!"
                          "As a result of your speedruning, you gain an extra heart!")
                    heart += 1
                    master_mode = "1"
                else:
                    print("you died :(")
                    restart = input("do you want to restart? y/n ")
                    if restart == "y":
                        master_mode = "y"
                    else:
                        print("ending")
                        done = True

            elif master_mode == "C":
                success = random.randrange(2)
                if success == 0:
                    print("you killed a bunch of bokoblins, now what?")
                    master_mode = "y"
                else:
                    print("You were struck by lightning for being evil")
                    restart = input("do you want to restart? y/n ")
                    if restart == "y":
                        master_mode = "y"
                    else:
                        print("ending")
                        done = True
            elif master_mode == "D":
                success = random.randrange(100)
                if success == 0:
                    print("YOU SURVIVED!!!!!! HOW")
                else:
                    print("You died :(")
                    restart = input("do you want to restart? y/n ")
                    if restart == "y":
                        master_mode = "y"
                    else:
                        print("ending")
                        done = True
            elif master_mode == "E":
                print("Ok, quitting now")
                done = True
            elif master_mode == "Banana":
                heart = 10000
                stamina = 10000
                weapons = 10000
                master_mode = "y"
            if master_mode == "1":
                print("\nYou find a statue and you can either get a heart or stamina vessel.")
                upgrade = input("Do you trade the spirit orbs for stamina or hearts? ")
                if upgrade == "hearts":
                    print("\nyou recieved your heart")
                    heart += 1
                    story += 1
                elif upgrade == "stamina":
                    print("\nYou recieved your stamina vessel")
                    stamina += 1
                    story += 1
                if upgrade == "hearts" or "stamina":
                    print("\nyou finished the great plateau, and con explore the rest of hyrule!")
                    select = input("""Do you:
                    A: Go to Kakariko village and talk to impa
                    
                    - """)
                    if select == "A":
                        print("Inpa says you must slay 4 divine beasts and free the champions")
                        master_mode = input("Do you want to slay the divine beasts? y/n ")
                        if master_mode == "y" and heart >= 3:
                            print("""You narrowly defeat the first divine beast and gain a power up,
                            you gain the ability to revive once when you die!""")
                            print("You gain a heart!")
                            heart += 1
                            champion_ability += 1
                            grace_uses = 1
                            story += 1
                            master_mode = "s"
                while master_mode == "s":
                    select = input("""Do you:
                    A: Fight gannon
                    B: Explore hyrule
                    C: Kill monsters
                    D: Search for more shrines
                    E: Quit
                    F: Check Progress
                    
                    - """)
                    if select == "A":
                        if heart <= 13 and story < 6:
                            cont = input("Are you sure? your hearts are very low, and you haven't completed "
                                         "everything y/n ")
                            if cont == "y":
                                print("Ok then")
                                rng = random.randrange(100)
                                if rng == 0:
                                    print("""Your luck is insane... YOU WIN
                                    Zelda is freed and hyrule is restored to peace
                                    
                                    
                                    
                                    for now""")
                                    break
                                else:
                                    print("You died")
                                    restart = input("do you want to restart? y/n ")
                                    if restart == "y":
                                        master_mode = "s"
                                    else:
                                        print("ending")
                                        break
                            elif cont == "n":
                                print("ok, returning to selection")
                                master_mode = "s"
                        else:
                            print("""All of your work has lead to this,
                                  You enter the castle ready to face gannon
                                  You enter the sanctum and cannon pulls you deeper into the caste
                                  the battle is hard, but you prevail!
                                  Gannon enters his final form... Dark Beast Gannon
                                  Princess zelda gives you the bow of light to finally put an end to gannon
                                  and together you and the princess defeat the beast and save hyrule...
                                  
                                  
                                  -For now...""")
                            break
                    elif select == "B":
                        outcome = random.randrange(4)
                        if outcome == 0:
                            print("You find a large cliff with loot on top")
                            scale = input("Do you attempt to scale the cliff? y/n ")
                            if scale == "y":
                                if champion_ability == 2:
                                    use_gale = input("Do you use your flying ability? y/n ")
                                    if use_gale == "y":
                                        print("You fly to the top and find the treasure, it's a weapon upgrade!")
                                        weapons += 1
                                        gale_uses -= 1
                                else:
                                    if stamina >= random.randrange(15):
                                        print("You scaled the cliff and found treasure, it's a weapon upgrade!")
                                        weapons += 1
                                    else:
                                        print("You fail to scale the cliff :(")
                                        master_mode = "s"
                            elif scale == "n":
                                print("Ok returning to selection screen")
                                master_mode = "s"
                        if outcome == 1:
                            print("You stumble across a chest!")
                            rng = random.randrange(100)
                            if rng == 0:
                                print("YOU FOUND A HEART!!!!!!")
                                heart += 1
                                print("Returning to selection")
                            if rng == 69:
                                print("Your rng is 69... niceeee")
                                heart += 100
                                stamina += 100
                                master_mode = "s"
                            else:
                                print("You found a weapon!")
                                weapons += 1
                                master_mode = "s"
                        if outcome == 2:
                            print("You were struck by lightning!")
                            if heart <= 10:
                                if grace_uses == 1:
                                    print("You were saved by your revive ability! but you lost it's use")
                                    grace_uses = 0
                                    master_mode = "s"
                                elif grace_uses == 0:
                                    print("You died :(")
                                    restart = input("do you want to restart? y/n ")
                                    if restart == "y":
                                        master_mode = "s"
                                    else:
                                        print("ending")
                                        break
                            else:
                                print("Your sheer number of hearts tanked the damage!")
                        if outcome == 3:
                            rest = input("You found a campfire, do you rest at it? y/n ")
                            if rest == "y":
                                print("You regained your abilities!")
                                grace_uses = 1
                                gale_uses = 3
                                master_mode = "s"
                    elif select == "C":
                        monster = random.randrange(10)
                        if monster <= 2:
                            print("You encounter a bokoblin")
                            fight = input("Do you want to fight it? y/n ")
                            if fight == "y":
                                if heart >= 3:
                                    print("You defeated the bokoblin, but it didn't give you anything useful")
                                    master_mode = "s"
                            else:
                                print("Ok returning to selection")
                                master_mode = "s"
                        elif monster > 2 <= 5:
                            print("You encounter a moblin")
                            fight = input("Do you want to fight it? y/n ")
                            if fight == "y":
                                if heart >= 5 and weapons >= 1:
                                    print("You defeated the moblin and found a weapon!")
                                    weapons += 1
                                    master_mode = "s"
                                else:
                                    print("You died :(")
                                    restart = input("do you want to restart? y/n ")
                                    if restart == "y":
                                        master_mode = "s"
                                    else:
                                        print("ending")
                                        break
                        elif monster > 5 < 9:
                            print("You encounter a lizalfos")
                            fight = input("Do you want to fight it? y/n ")
                            if fight == "y":
                                if heart >= 5 and weapons >= 1:
                                    print("You defeated the lizalfos and found a weapon!")
                                    weapons += 1
                                    master_mode = "s"
                                else:
                                    print("You died :(")
                                    restart = input("do you want to restart? y/n ")
                                    if restart == "y":
                                        master_mode = "s"
                                    else:
                                        print("ending")
                                        break
                        elif monster == 9:
                            print("You encounter a lynel")
                            fight = input("Do you want to fight it? y/n ")
                            if fight == "y":
                                if fury_uses < 0:
                                    instant_kill = input("Do you want to use your fury ability to "
                                                         "instant kill this enemy? y/n ")
                                    if instant_kill == "y":
                                        print("You killed the lynel and gained many weapons")
                                        weapons += 3
                                    else:
                                        if heart >= 13 and weapons >= 8:
                                            print("You defeated the lynel and found multiple weapons!")
                                            weapons += 3
                                            master_mode = "s"
                                        else:
                                            print("You died :(")
                                            restart = input("do you want to restart? y/n ")
                                            if restart == "y":
                                                master_mode = "s"
                                            else:
                                                print("ending")
                                                break
                                if heart >= 13 and weapons >= 8:
                                    print("You defeated the lynel and found multiple weapons!")
                                    weapons += 3
                                    master_mode = "s"
                                else:
                                    print("You died :(")
                                    restart = input("do you want to restart? y/n ")
                                    if restart == "y":
                                        master_mode = "s"
                                    else:
                                        print("ending")
                                        break
                    elif select == "D":
                        shrine = random.randrange(5)
                        if shrine == 0:
                            print("You don't find a shrine :(")
                            master_mode = "s"
                        elif shrine == 1:
                            print("You find a shrine with an enemy inside")
                            fight = input("Do you want to fight it? y/n ")
                            if fight == "y":
                                print("You enter the shrine")
                                if heart >= random.randrange(4, 13):
                                    print("You defeated the enemy!")
                                    print("\nYou find a statue and you can either get a heart or stamina vessel.")
                                    upgrade = input("Do you trade the spirit orbs for stamina or hearts? ")
                                    if upgrade == "heart" or "hearts":
                                        print("You gain your heart!")
                                        heart += 1
                                    elif upgrade == "stamina":
                                        print("You recieve your stamina vessel")
                                        stamina += 1
                                else:
                                    print("You died :(")
                                    restart = input("do you want to restart? y/n ")
                                    if restart == "y":
                                        master_mode = "s"
                                    else:
                                        print("ending")
                                        break
                        elif shrine == 2:
                            riddle = input("I’m tall when I’m young, and I’m short when I’m old. What am I? ")
                            if riddle == "a candle" or "A candle":
                                print("Correct!")
                                print("\nYou find a statue and you can either get a heart or stamina vessel.")
                                upgrade = input("Do you trade the spirit orbs for stamina or hearts? ")
                                if upgrade == "hearts":
                                    print("You gain your heart!")
                                    heart += 1
                                elif upgrade == "stamina":
                                    print("You recieve your stamina vessel")
                                    stamina += 1
                            else:
                                print("Wrong answer :(")
                        elif shrine == 3:
                            number_1 = random.randrange(1, 11)
                            math = input("Pick a number between 1 and 10 ")
                            if number_1 == math:
                                print("correct!")
                                print("\nYou find a statue and you can either get a heart or stamina vessel.")
                                upgrade = input("Do you trade the spirit orbs for stamina or hearts? ")
                                if upgrade == "heart" or "hearts":
                                    print("You gain your heart!")
                                    heart += 1
                                if upgrade == "stamina":
                                    print("You recieve your stamina vessel")
                                    stamina += 1
                            else:
                                print("Wrong :(")
                        elif shrine == 4:
                            print("\nYou find a statue and you can either get a heart or stamina vessel.")
                            upgrade = input("Do you trade the spirit orbs for stamina or hearts? ")
                            if upgrade == "heart" or "hearts":
                                print("You gain your heart!")
                                heart += 1
                            elif upgrade == "stamina":
                                print("You recieve your stamina vessel")
                                stamina += 1
                    elif select == "E":
                        quit_game = input("Are you sure you want to quit? y/n ")
                        if quit_game == "y":
                            print("Quitting now")
                            break
                        else:
                            print("Returning to selection")

                    elif select == "F":
                        print("You have completed", int(story), "out of 6 objectives")
                        print("You have", int(heart), "hearts")
                        print("You have", int(weapons), "weapons")
                        if story == 1:
                            print("Inpa says you must slay 4 divine beasts and free the champions")
                            master_mode = input("Do you want to slay the divine beasts? y/n ")
                            if master_mode == "y" and heart >= 4:
                                print("""You narrowly defeat the first divine beast and gain a power up,
                                                        you gain the ability to revive once when you die!""")
                                print("You gain a heart!")
                                heart += 1
                                champion_ability += 1
                                grace_uses = 1
                                story += 1
                                master_mode = 2
                            if master_mode == "y" and weapons >= 1:
                                print(
                                    """The boss gave you a bit of challenge, but it was no match for your upgraded weapons""")
                                print("you gain the ability to revive once when you die!")
                                print("You gain a heart!")
                                heart += 1
                                story += 1
                                champion_ability += 1
                                grace_uses = 1
                        elif story == 2:
                            cont = input("do you want to try to complete the next divine beast? y/n ")
                            if cont == "y":
                                confirm = input("""\nyou enter the next divine beast, this one seems to be a harder challenge...
                                        are you sure you don't want to explore hyrule before tackling this challenge? y/n """)
                                if confirm == "y":
                                    print("Good luck!")
                                    if heart >= 7 and weapons >= 1:
                                        print("You succeeded in defeating the beast, nice work!")
                                        print("You gain a heart and the ability to leap high in the air!")
                                        heart += 1
                                        champion_ability += 1
                                        story = 3
                                    if heart >= 5 and weapons >= 2:
                                        print("You succeeded in defeating the beast, nice work!")
                                        print("You gain a heart and the ability to leap high in the air!")
                                        heart += 1
                                        champion_ability += 1
                                        story = 3
                                        master_mode = "s"
                                    else:
                                        print("You died")
                                        restart = input("do you want to restart? y/n ")
                                        if restart == "y":
                                            master_mode = "s"
                                        else:
                                            print("ending")
                                            break
                                if confirm == "n":
                                    print("Ok, returning to selection screen")
                                    master_mode = "s"
                            elif cont == "n":
                                print("Ok returning to selection!")
                                master_mode = "s"
                        elif story == 3:
                            confirm = input("""\nyou enter the next divine beast, this one seems to be a harder 
                            challenge... are you sure you don't want to explore hyrule before tackling this 
                            challenge? y/n """)
                            if confirm == "y":
                                print("Ok, entering the divine beast")
                                if heart >= 10 and weapons >= 5:
                                    print("The monster stopping you from freeing this beast proved to be a challenge,"
                                          "but you slew the beast and gained a heart and another ability!"
                                          "You can now create lightning around you and instantly kill certain enemies!")
                                    story += 1
                                    heart += 1
                                    fury_uses = 3
                                    champion_ability += 1
                                else:
                                    print("The monster was too powerful and you died :("
                                          "Maybe try looking for some shrines")
                                    restart = input("do you want to restart? y/n ")
                                    if restart == "y":
                                        master_mode = "s"
                                    else:
                                        print("ending")
                                        break
                        elif story == 4:
                            confirm = input("""\n This is the final divine beast, are you sure you want to continue?
                                                   If you don't have at least 10 weapons then you should explore 
                                                   hyrule more. y/n """)
                            if confirm == "y":
                                print("Ok, entering the divine beast")
                                if heart >= 10 and weapons >= 5:
                                    print("The monster stopping you from freeing this beast proved to be a challenge,"
                                          "but you used your skills and vast arsenal of weapons to slay the final divine beast"
                                          "You can now block 3 powerful attacks with a force field!")
                                    story += 1
                                    heart += 1
                                    protection_uses = 3
                                    champion_ability += 1
                                else:
                                    print("The monster was too powerful and you died :("
                                          "Maybe try looking for some shrines")
                                    restart = input("do you want to restart? y/n ")
                                    if restart == "y":
                                        master_mode = "s"
                                    else:
                                        print("ending")
                                        break

                        elif story == 5:
                            print("A strange voice calls to you..."
                                  "\nLink... go to the korok forest, a trial awaits you there"
                                  "pass the trial and you will be ready to face gannon and save the princess")
                            cont = input("\n Do you want to travel to the korok forest? ")
                            if cont == "y":
                                print("You travel to the forest and see a path illuminated by fire..."
                                      "You get to the end of the path but there is nothing there..."
                                      "it's as if there is an invisible path for you to go on...")
                                direction = input("Do you go forward left or right? ")
                                if direction == "forward":
                                    direction2 = input("Do you want to go forward left or right? ")
                                    if direction2 == "left":
                                        direction3 = input("Do you want to go forward left or right? ")
                                        if direction3 == "forward":
                                            direction4 = input("Do you want to go forward left or right? ")
                                            if direction4 == "right":
                                                master_sword = input("You reach another past and you enter the "
                                                                     "korok forest... "
                                                                     "You see a sword in front of you... do you take it? y/n ")
                                                if master_sword == "y":
                                                    print("You take the sword out of the ground..."
                                                          "It's blue glow can eradicate evil..."
                                                          "You acquired the master sword!"
                                                          "Now you can defeat ganon and save zelda!")
                                                    story += 1
                                                else:
                                                    print("Why wouldn't you take the sword lol")
                                            else:
                                                print("you went the wrong way :(")
                                        else:
                                            print("you went the wrong way :(")
                                    else:
                                        print("you went the wrong way :(")
                                else:
                                    print("you went the wrong way :(")




main()
