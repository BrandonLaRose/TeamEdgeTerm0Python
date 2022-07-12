#********************************************************************
 #                                                                 
 #  Team Edge List Mini-project: THE SHOPPING LIST HELPER
 # 
 #  This project prompts users using input() to prompt users
 #  to add (or remove) items from a shopping list. It starts empty
 #  and each time the program is run it asks you to either add or 
 #  remove an item from the list. It also updates the user of its
 #  contents. The shopping list also checks to see if an item 
 #  is already present in the list and prevents you from adding it
 #  again, giving feedback along the way. 
 # 
 # ***************************************************************/
reply = ""
active = True
add_in = ""
remove_in = ""
print("Welcome to Shopping List!")

welcome_message = "Hi! I'm your shopping assistant. Let me take your order. \nYou can type 'add milk' to add milk to your shopping list. \nor you can type 'remove milk' to remove it. \n"

print(welcome_message)


#-->Todo: declare a shopping_list list

shopping_list = ["apple", "bread", "milk", "eggs", "chips", "cookies"]



def prompt_user():

    reply = input("Do you want to add or remove something from the shopping list?  >>  ")
    

       
      
    
    
      

    return reply

def check_answer(ans):
  if remove_in in shopping_list:
    print("Removing the item from your shopping list")
    shopping_list.remove(remove_in)
  elif remove_in not in shopping_list:
    print("The item you want to remove is not on the shopping list")
    prompt_user()
  elif add_in in shopping_list:
    print("This is already in your cart!")
    prompt_user()
  elif add_in not in shopping_list:
    print("adding the item to your shopping list")
    shopping_list.append(add_in)
    
    
  pass
    
# https://sites.google.com/csedge.org/team-edge-web-python/term-0/lab-5-lists?authuser=0

def add_item():
  
  if reply == "add":
      add_in = input("What would you like to add to the shopping list? ")
      shopping_list.append(add_in)
    
  pass
  


def remove_item():
  
  if reply == "remove":
      remove_in = input("What item would you like to remove from the shopping list? ")

  return remove_in
  pass

while active:

    check_answer(prompt_user()) #this makes the program continously prompt and check response while the boolean 'active' returns True
 