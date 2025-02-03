# pre defines
adjs = [
    "Savage", "Ruthless", "Chill", "Deadly", "Fearless", "Epic", "Twisted", 
    "Dark", "Icy", "Frosty", "Blazing", "Vicious", "Radical", "Funky", 
    "Insane", "Silent", "Grim", "Reckless", "Wicked", "Shadowy",
    "Infinite", "Legendary", "Mythic", "Daring", "Dynamic", "Cunning", 
    "Electric", "Neon", "Phantom", "Rogue", "Venomous", "Glitched", 
    "Quantum", "Atomic", "Lethal", "Toxic", "Hypnotic", "Sinister", 
    "Cyber", "Doomed", "Infernal",
    "Stealthy", "Elite", "Spiky", "Snazzy", "Flashy", "Fiery", "Glowing", 
    "Sharp", "Lunar", "Solar", "Stormy", "Warped", "Eternal", "Blazing", 
    "Cosmic", "Frozen", "Mighty", "Funky", "Edgy", "Loyal",
    "Savvy", "Fierce", "Dapper", "Slick", "Raging", "Vivid", "Shiny", 
    "Zesty", "Perky", "Chill", "Bold", "Cozy", "Killer", "Quirky", 
    "Funky", "Stellar", "Dynamic", "Spooky", "Iron", "Golden"
]


nouns = [
    "Slayer", "Rogue", "Sniper", "Shadow", "Hunter", "Phantom", "Beast", 
    "Dragon", "Titan", "Eagle", "Falcon", "Fox", "Wolf", "Raven", "Blaze", 
    "Viper", "Comet", "Flare", "Storm", "Nebula",
    "Glitch", "Knight", "Cyber", "Dagger", "Blizzard", "Circuit", 
    "Drone", "Matrix", "Pixel", "Warden", "Nomad", "Valkyrie", 
    "Witch", "Oracle", "Guardian", "Seeker", "Warrior", "Ranger", "Reaper", 
    "Swordsman",
    "Rocket", "Laser", "Synth", "Bot", "Gear", "Cypher", "Quantum", 
    "Galaxy", "Bolt", "Beacon", "Code", "Striker", "Challenger", "Fighter", 
    "Survivor", "Scout", "Raider", "Chaser", "Champion", "Explorer",
    "Pirate", "Sailor", "Hero", "Villain", "Pathfinder", "Gambler", 
    "Visionary", "Dreamer", "Creator", "Nomad", "Stalker", "Voyager", 
    "Crusader", "Rebel", "Legend", "Thorn", "Reactor", "Spark", 
    "Dominator", "Hacker"
]


digs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


spl_chars = [
    "_", "-", ".", "~", "!", "@", "#", "$", "%", "&", "*", "+", 
    "=", "|", "^", ">", "<"
]


# Functionaing Code
import random
while True:
    # Random Choices
    N=random.choice(nouns)
    A=random.choice(adjs)
    D=random.choice(digs)
    S=random.choice(spl_chars)

    # Adding Preferences
    while True:
        inp=input("Y for Yes \nN for No \nDo you want to add preferences:").lower()
        if inp=="y":
            UIN=input("Enter preference here: ")
            U_IN=("_"+UIN+"_")
            nme=[N,A,D,S,U_IN]
            break
        elif inp=="n":
            nme=[N,A,D,S]
            break
        else:
            print("Invalid input. Please enter Y or N.")


    # Randomizing the order in username
    random.shuffle(nme)
    username="".join(nme)

    #File handling and checking for existing names
    f=open("names.txt","r")
    existing_name=f.read().splitlines()

    if username in existing_name:
        print(f"Username '{username}' already exists!\nGo again!")
        continue
    else:
        f=open("names.txt","a")
        f.write(username+"\n")
        f.close
        break
# Printing the username
print(f"Username Generated!\nUsername: {username}")

