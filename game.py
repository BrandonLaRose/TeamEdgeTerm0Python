#################################################
# Code Tutorial
#
#Random items in everyroom?
#
#
# sword(good), pet-tiger(good), poison(bad), books(good), (knife), bottle of blood(good),
#
#3 items of each room
#
# https://sites.google.com/csedge.org/team-edge-web-python/term-0/lab-78-dictionaries/project-choose-your-own-adventure?authuser=0
###################################################

import os
#os.system("clear")

## TO DO
# 
welcome_prompt = ("wElcoMe t0 mY coll3ct G@me")
print(welcome_prompt)

username = input("\nEnter username:")
print("Welcome " + username)

print("There are 4 rooms you are able to navigate in, start in whichever room you want dude\n")

print("Welcome to the game, you are now going to choose a room: \n")


rooms = ["Gym", "Courtyard", "Bigoyard", "Laboratory"]

Courtyard = ["cat","dog"]
Gym = ["barbell","sword"]
Laboratory = ["tiger", "potion", "magic wand"]
Bigoyard = ["books", "shoes", "disco-ball"]

inventory = []

def enterGym():
  os.system("clear")
  print("Welcome to the gym!!!")
  print("Gym Items:\n")
  for item in Gym:
    print(item)
  gymItem = input("\nChoose an item:")
  if gymItem in Gym:
    inventory.append(gymItem)
    print(gymItem+" chosen!")
    print("Inventory:" + str(inventory))
  else:
    print("This item isn't in this room!")
  
def enterCourtYard():
  os.system("clear")
  print("Welcome to the courtyard!!")
  print("Courtyard Items:")
  for item in Courtyard:
    print(item)
  courtyardItem = input("\nChoose an item:")
  if courtyardItem in Courtyard:
    inventory.append(courtyardItem)
    print(courtyardItem + " chosen!")
    print("Inventory:" + str(inventory))
  
def enterBigoyard():
  os.system("clear")
  print("Welcome to the Bigoyard!")
  print("Bigoyard items:")
  for item in Bigoyard:
    print(item)
  bigoyardItem = input("\nChoose an item:")
  print(bigoyardItem + " chosen!")
  if item in Bigoyard:
    inventory.append(item)
    print(item + " chosen!")
    print("Inventory:" + str(inventory))
      
def enterLabortory():
  os.system("clear")
  print("Welcome to the Laboratory!")
  print("Laboratory items:")
  for item in Laboratory:
    print(item)
  labItem = input("\nChoose an item:")
  print(labItem + " chosen!")
  if item in Laboratory:
    inventory.append(item)
    print(item + " chosen!")
    print("Inventory:" + str(inventory))


print("Rooms")
for room in rooms:
  print(room)


while True:   
  
  pickedRoom = input("\nChoose a room:")
  if(pickedRoom not in rooms):
    print("Room not valid dude :(")
  
  if(pickedRoom == "Gym"):
    enterGym()

  if(pickedRoom == "Courtyard"):
    enterCourtYard()
  
  if(pickedRoom == "Laboratory"):
    enterLabortory()

  if(pickedRoom == "Bigoyard"):
    enterBigoyard()




  


  
