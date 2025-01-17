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

import random

# N=random.randint(0,100)
# A=random.randint(0,100)
# D=random.randint(0,10)
# S=random.randint(0,32)

N=random.choice(nouns)
A=random.choice(adjs)
D=random.choice(digs)
S=random.choice(spl_chars)

# username=nouns[N]+adjs[A]+digs[D]+spl_chars[S]
username=N+A+D+S
print(username)


# print(len(adjs))
# print(len(nouns))
# print(len(digs))
# print(len(spl_chars))
