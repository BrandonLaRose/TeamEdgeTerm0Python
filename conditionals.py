
# -------------------------------------------- 
# Day 2 Challenges
# -------------------------------------------- 

message = "Welcome to Day 2.\nToday we are learning about conditionals.\nLet's practice writing some conditionals of our own!"
print(message)
# -------------------------------------------- 

print("------------------- Challenge 1 -------------------")
# Can you drive?
   # Prompt the user to enter their age.
   # Write conditional statements that print out whether you can drive in your city. 
age = input("Enter Age: ")
if int(age) >= (16):
   print("Can drive!")
else:
   print("You're too young!")











# -------------------------------------------- 

print("------------------- Challenge 2 -------------------") 

# Who placed first?
   # Write conditional statements that checks which is the highest and prints the highest score. 
   # Hint: Create three variables and assign them random scores. 
from random import randint
score1=randint(1,100)
score2=randint(1,100)
score3=randint(1,100)
top=score1
high=(str)
if score1 > score2 and score1 > score3:
   top=score1
   high="Score 1"
elif score2 > score3:
   top=score2
   high="Score 2"
else:
   top=score3
   high="Score 3"
#print(score1)
#print(score2)
#print(score3)
print(top)










# -------------------------------------------- 

print("------------------- Challenge 3 -------------------")

# One of the most common parts of our daily routine is checking the weather. 
# Our outfit and accessories are dependent on the temperature and conditions outside. 
# ie. We're probably not going to wear shorts out when it's snowing...


# **** Challenge 3: Part 1 ****
# Write a conditional statement that checks the value of the weather variable 
# and prints out a weather report based on the current weather:
# Rainy: Bring an umbrella
# Sunny: Wear a hat and sunglasses
# Snowing: Wear gloves and a scarf 

# Here's a variable to get you started:
weather = "rainy"
if weather == "rainy":
   print(f"Make sure to bring an umbrella since it's {weather}")
elif weather == "sunny":
   print(f"Make sure to wear a hat and sunglasses since it's {weather}")
else:
   print(f"Make sure to wear gloves and a scarf since it's {weather}")













# Tip: Try changing the value of the weather variable to test your other conditions.

# **** Challenge 3: Part 2 ****
# Now that you've written conditions for specific weather forecasts, let's also add in temperature! 
# You can't dress accordingly if you only know that it's raining outside but not how cold it is!
# For example:
    # If it's raining and 60 degrees, you might want to bring your umbrella and wear a light jacket.
    # However, if it's raining and 30 degrees, you might want to break out a warmer jacket with your umbrella instead. 
    
   # Add to your conditional statements above and modify your weather reports to also take into account the temperature. 
   # Make sure to account for at least three different temperatures!
   # Hint: You will need another variable to keep track of the temperature.
temp=90
if temp >= 75:
   print(f"Youre gonna want to probably wear shorts since its {temp} out!")
elif temp >= 60:
   print(f"Additionaly, you're gonna want to probably wear a like jacket since its {temp} out!")
else:
   print(f"Youre gonna want to probably wear a heavier jacket since its {temp} out!")














# -------------------------------------------- 

print("------------------- Challenge 4 -------------------")

# Prompt the user to enter the day of the week (1-7 representing Monday - Sunday)
# Write a set of conditionals that will take a number from 1 to 7 
# and print out the corresponding day of the week. 
# Make sure to add a statement that accounts for any numbers out of range! 
day = input("Enter a number for the day of week: ")
if int(day) == 1:
   print("It's Sunday")
elif int(day) == 2:
   print("It's Monday")
elif int(day) == 3:
   print("It's Tuesday")
elif int(day) == 4:
   print("It's Wednesday")
elif int(day) == 5:
   print("It's Thursday")
elif int(day) == 6:
   print("It's Friday")
elif int(day) == 7:
   print("It's Saturday")
else:
   print("What are you doing? Theres only 7 days in a week")










# -------------------------------------------- 

print("------------------- Challenge 5 -------------------")

# A leap year is a calendar year that contains an additional day added 
# to keep the calendar year synchronized with the astronomical year or seasonal year.
# To calculate if a specific year is/was a leap year, you can follow the following steps:
     # 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
     # 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
     # 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
     # 4. The year is a leap year (it has 366 days).
     # 5. The year is not a leap year (it has 365 days).

# Those are a lot of conditions...
# Your challenge is to translate the steps above into conditionals which will evaluate if the 
# year stored in a variable is/was a leap year.

year=30000
if year % 4 == 0:
   if year % 100 == 0:
      if year % 400 == 0:
         print("There are 366 days this year (It's a leap year)")
else:
   print("It's not a leap year. There's 365 days this dear.")





