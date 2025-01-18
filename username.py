# pre defines
adjs = [
    "Brave", "Clever", "Witty", "Fierce", "Mighty", "Lively", "Swift", 
    "Bold", "Silent", "Happy", "Curious", "Epic", "Shiny", "Zesty", 
    "Lucky", "Rustic", "Frosty", "Cheerful", "Cosmic", "Vibrant",
    "Noble", "Mystic", "Daring", "Ancient", "Glowing", "Ethereal", 
    "Enchanted", "Legendary", "Sacred", "Magical", "Luminous", 
    "Celestial", "Shadowy", "Divine", "Unseen", "Mythical", 
    "Shimmering", "Golden", "Arcane", "Infinite",
    "Stormy", "Icy", "Blazing", "Thorny", "Verdant", "Sunny", 
    "Frozen", "Wavy", "Breezy", "Rainy", "Dusky", "Windy", 
    "Foggy", "Wild", "Rocky", "Starry", "Crimson", "Azure", 
    "Emerald", "Amber",
    "Quantum", "Neon", "Robotic", "Synthetic", "Digital", 
    "Galactic", "Chrome", "Viral", "Electric", "Virtual", 
    "Dynamic", "Reactive", "Augmented", "Automated", "Coded", 
    "Cybernetic", "Holographic", "Cosmic", "Energized", "Advanced",
    "Snappy", "Zany", "Epic", "Vivid", "Playful", "Fancy", 
    "Gentle", "Swift", "Mellow", "Bold", "Sharp", "Chilly", 
    "Cozy", "Whimsical", "Perky", "Quirky", "Radiant", 
    "Elegant", "Stellar", "Brilliant"
]

nouns = [
    "Falcon", "Wolf", "Eagle", "Phoenix", "Panther", "Bear", "Tiger", "Fox", 
    "Raven", "Owl", "Comet", "Star", "Storm", "Glacier", "River", "Shadow", 
    "Thorn", "Forest", "Blizzard", "Flame",
    "Wizard", "Knight", "Dragon", "Titan", "Elf", "Goblin", "Valkyrie", 
    "Unicorn", "Warden", "Sorcerer", "Oracle", "Witch", "Bard", "Dagger", 
    "Archer", "Wanderer", "Mystic", "Guardian", "Paladin", "Seeker",
    "Circuit", "Atom", "Cypher", "Pixel", "Rocket", "Drone", "Satellite", 
    "Nexus", "Matrix", "Quantum", "Bot", "Gear", "Laser", "Synth", "Ray", 
    "Beacon", "Byte", "Code", "Reactor", "Galaxy",
    "Hunter", "Warrior", "Ranger", "Sniper", "Swordsman", "Gladiator", 
    "Crusader", "Raider", "Assassin", "Nomad", "Protector", "Chaser", 
    "Fighter", "Scout", "Jumper", "Challenger", "Striker", "Survivor", 
    "Champion", "Rebel",
    "Pirate", "Captain", "Sailor", "Voyager", "Rider", "King", "Queen", 
    "Monarch", "Hero", "Villain", "Gambler", "Scholar", "Architect", 
    "Pioneer", "Visionary", "Nomad", "Pathfinder", "Creator", "Dreamer", 
    "Explorer"
]

digs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


spl_chars = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", 
    "=", "+", "{", "}", "[", "]", "|", "\\", ":", ";", "\"", "'", 
    "<", ">", ",", ".", "?", "/", "~", "`"
]


# random
import random

N=random.choice(nouns)
A=random.choice(adjs)
D=random.choice(digs)
S=random.choice(spl_chars)

inp=input("Y for Yes \nN for No \nDo you want to add preferences:")
inp=inp.lower()
if inp=="y":
    UIN=input("Enter preference here: ")
    U_IN=("_"+UIN+"_")
    nme=[N,A,D,S,U_IN]
elif inp=="n":
    nme=[N,A,D,S]
else:
    print("Please enter Y or N.")


random.shuffle(nme)
username="".join(nme)

f=open("names.txt","a")
f.write(username+"\n")
f.close

f=open("names.txt","r")
print(f.read())

