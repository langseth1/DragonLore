#DragonLore A Game Created By Fury. PS: This Application Will Not Send Your Name

print("Enter a name.")
name = input()
if name != "":
    print("Thank you for entering a name")
else:
    print("You Did Not Enter A Name")

print("DragonLore a Game by Fury")
myName = input("if you want to start the game press[Y]")
if(myName == "y"):
    print("Loading DragonLore...")
    print("Finished")
myCharacter = input("Choose Your Character [1] For WIZARD [2] For GIANT [3] For WITCH")
if(myCharacter == "1"):
    print("You choose WIZARD")
elif(myCharacter == "2"):
    print("You choose GIANT")
elif(myCharacter == "3"):
    print("You choose WITCH")
print("Entering DragonCity")
myChoice = input("You are currently in a weapon store, Do you want to buy anything? Press [1] to buy a Sword, Press [2] to buy a Axe.")
if(myChoice == "1"):
    print("You Bought a Sword")
elif(myChoice == "2"):
    print("You Bought a Axe")
print("Exiting the store")
compass = input("What Direction do you want to go in, Press [N] for North, Press [S] for south")
if(compass == "N"):
    print("You Choose North")
elif(compass == "S"):
    print("You Choose South")
youMeet = input("You meet on a goblin that's aggresive to you, Do you want to attack[Y] or do you want to run[N]")
if(youMeet == "y"):
    print("You Attacked the goblin the goblin hits you and you hit the goblin the goblin dies, You are now at 76HP")
elif(youMeet == "n"):
    print("You ran from the goblin and the goblin almost hit you but missed, You ran away.")
print("Entering LoreCity...")
print("You Have Entered LoreCity!")
way = input("Where do you want to go the potion store[1] or the cafe[2]?")
if(way == "1"):
    print("You Have Entered The Potion Store!")
elif(way == "2"):
    print("You Have Entered The Cafe")
