import random

# -------------------------------------------- 

	# You've just learned about variables, conditionals.
	# Just from knowing those two topics, you can do so much!
	
	# Let's try to make a simple program that responds to the user.
	# We're going to recreate the Magic 8 Ball!!!
			
			# Never heard of it? You suck!

					# You got this...Sike!

  # -------------------------------------------- 

	# How a Magic 8 Ball Works:

	# The user asks a question and vigoriously shakes the ball. 
	# Then the ball will respond with one of twenty responses, chosen at random. 

	# That's pretty simple right?

 # -------------------------------------------- 

	# Part 1: 
	# Print instructions on the screen and 
	# prompt the user to ask a question

	

  # --------------------------------------------


print("Ask anything and the magic 8ball will respond")
input("Ask a question or something: ")








import random




# -------------------------------------------- 

	# Part 2: Next, we need to randomly select a response from 20 options.

	# Randomly select a number from 0 - 19 
	# Use that to select from the following responses:
t0 = "It is certain."
t1 = "It is decidedly so."
t2 = "Without a doubt."
t3 = "Yes - definitely."
t4 = "You may rely on it."
t5 = "As I see it, yes."
t6 = "Most likely."
t7 = "Outlook good."
t8 = "Yes."
t9 = "Signs point to yes."
t10 = "Reply hazy, try again."
t11 = "Ask again later."
t12 = "Better not tell you now."
t13 = "Cannot predict now."
t14 = "Concentrate and ask again."
t15 = "Don't count on it."
t16 = "My reply is no."
t17 = "My sources say no."
t18 = "Outlook not so good."
t19 = "Very doubtful."

	# Look up random.rand_int to see how you can use it to select a random number.

  # -------------------------------------------- 
outcome=(random.randint(0, 19))
print(vars("t"+str(outcome)))



















# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# -------------------------------------------- 

















