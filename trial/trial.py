# pre defines
adjs = ["Brave"]
nouns = ["Falcon"]
digs = ["0"]
spl_chars = ["@"]


# random
import random

while True:
    N=random.choice(nouns)
    A=random.choice(adjs)
    D=random.choice(digs)
    S=random.choice(spl_chars)


# Appending Preferences
    while True:
        inp=input("Y for Yes \nN for No \nDo you want to add preferences:").lower()
        if inp=="y":
            UIN=input("Enter preference here: ")
            U_IN=("_"+UIN+"_")
            nme=[N,A,U_IN]
            break
        elif inp=="n":
            nme=[N,A]
            break
        else:
            print("Invalid input. Please enter Y or N.")


    # Randomizing the order in username
    random.shuffle(nme)
    username="".join(nme)

    # Already existinng check
    f=open("all_names.txt","r")
    existing_names=f.read().splitlines()

    if username in existing_names:
        print(f"Username '{username}' already exists!\nGo again!")
        continue
    else:
        f=open("all_names.txt","a")
        f.write(username+"\n")
        f.close
        break
    
# # Printing the username
# f=open("names.txt","r")
# print(f.read())

print(f"Username Generated!\nUsername: {username}")

