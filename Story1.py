from Getters import *
from Screen import *
import os

def Story1(debug = False):
	if debug: print("Story 1 Function")
	
	playerName = getMadlibOption("Enter your name: ", debug)
	thing1 = getMadlibOption("Enter an object: ", debug)
	bodyPart = getMadlibOption("Enter an appendage: ", debug)
	place1 = getMadlibOption("Enter a place: ", debug)
	event1 = getMadlibOption("Enter an event: ", debug)
	decide = False
	while decide == False:
		yes = getMadlibOption("Enter yes or no: ", debug)
		if yes == "yes": 
			decide = True
			decision = "go over to it"
		elif yes == "no":
			decide = True
			decision = "run in the opposite direction"
		else:
			decide = False
	evilName = getMadlibOption("Enter another name: ", debug)
	number1 = getMadlibOptionNumber("Enter a number 1-10: ", 1, 10, debug)
	zeldaMonster = getMadlibOptionZeldaMonster("Enter Zelda enemy: ", debug)
	os.system("cls")
		
	
	out = "\n"
	out += playerName + " was walking in the woods when you spotted a " + thing1 + ".\n"
	out += "You walked over to it and suddenly a " + bodyPart + " grabbed him and dragged him undeneath the " + place1 + ".\n"
	out += "You saw some sort of " + event1 + " going on and decide to " + decision + ".\n"
	if yes == "yes":
		out += "As you walked over you realized that they were all " + evilName + " suddenly " + number1 + " " + evilName + "s jumped on you.\n"
		out += "You slam onto the ground and got the life sucked out of you by the " + evilName + "s like they were " + zeldaMonster + "s.\n"
		out += "\n"
		out += loseScreen(debug)
	elif yes == "no":
		out += "Suddenly " + number1 + " figures chased after you from the " + event1 + "\n"
		out += "As they got closer you realized that they were all " + evilName + ".\n"
		out += "Out of nowhere a " + zeldaMonster + " took out all of the " + evilName + "s.\n"
		out += "As you continued to run you finaly found the exit and made it out alive\n"
		out += "\n"
		out += winScreen(debug)
		
		
	return out
