from Getters import *
from Screen import *
import os

def Story2(debug = False):
	if debug: print("Story 2 Function")
	
	friendName = getMadlibOption("Enter a name: ", debug)
	vegtable1 = getMadlibOption("Enter a veggietable: ", debug)
	creature1 = getMadlibOption("Enter a creature: ", debug)	
	planet1 = getMadlibOption("Enter a planet: ", debug)
	store1 = getMadlibOption("Enter a store: ", debug)
	object1 = getMadlibOption("Enter a tool you would find in the store: ", debug)
	dirt1 = getMadlibOption("Enter a type of ground matter: ", debug)
	grandma1 = getMadlibOptionNumber("Enter an age 50-110: ", 50, 110, debug)
	grandma2 = getMadlibOption("Enter a hip name: ", debug)
	shoe1 = getMadlibOption("Enter a shoe: ", debug)
	decide = False
	while decide == False:
		yes = getMadlibOption("Should you let her in?, yes or no: ", debug)
		if yes == "yes": 
			decide = True
			decision = "yes"
		elif yes == "no":
			decide = True
			decision = "no"
		else:
			decide = False
	food1 = getMadlibOption("Enter a mealtime: ", debug)
	os.system("cls")
	
	out = "\n"
	out += "As you exit the cave you see your friend, " + friendName + ".  As you run up to greet him he stabs you with a " + vegtable1 + ".\n"
	out += "Then he shapeshifts into his true form, a " + creature1 + " from the planet " + planet1 + ".\n"
	out += "You start to run to the nearest " + store1 + " and the " + creature1 + " starts to run after you.\n"
	out += "It accidentally steps on the " + vegtable1 + " and slips eating " + dirt1 + ".\n"
	if store1.lower() == "mc donalds":
		out += "As you run to Mc Donalds the " + creature1 + " gets enticed by a Big Mac and runs into the store forgoing chasing you.\n"
		out += "A " + grandma1 + " year old grandma named " + grandma2 + " hits the " + creature1 + " with her brand new " + shoe1 + ".\n"
		out += "The " + creature1 + " starts to burn, since grandmas called " + grandma2 + " is its only weakness.\n"
		out += "\n"
		out += winScreen(debug)
	else:
		out += "You ran into " + store1 + " and shut the door grabing a " + object1 + " to block it with.\n"
		out += "The " + creature1 + " trys to break though the door but can't since the " + object1 + " is to strong.\n"
		out += "The " + creature1 + " walks away realizing that he won't be able to break in, then you see your grandma " + grandma2 + ".\n"
		if decision == "yes":
			out += "You decide to let your grandma in but then she shapeshifts and eats you like you were " + food1 + ".\n"
			out += "\n"
			out += loseScreen(debug)
		elif decision == "no":
			out += "She asks to come into the store, but you say no and then call the cops on her.\n"
			out += "As the the cops handcuff her and put her into their car you realize she wasn't the shapeshifter, oops.\n"
			out += "But hey, at least you didn't die.\n"
			out += "\n"
			out += winScreen(debug)
	
	return out
