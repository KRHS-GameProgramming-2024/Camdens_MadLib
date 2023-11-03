from Getters import *
from Screen import *
from Story3getter import *
import os
import time
import random

def Story3(debug = False):
	if debug: print("Story 3 Function")
	
	EvilName = getMadlibOption("Enter a name: ", debug)
	weapon = getWeapon("Enter a weapon: ", debug)
	dolphine = random.randint(1, 10)
	
	os.system("cls")
	print(Story3a(debug))
	print(EvilName + " approaches you")
	action = False
	while action == False:
		act = input("Attack or Defend, A/D: ")
		os.system("cls")	
		if act.lower() == "a":
			print(Story3acttack(debug))
			time.sleep(.2)
			os.system("cls")
			print(Story3b(debug))
			action = True
		elif act.lower() == "d":
			print(Story3d(debug))
			action = True
		else:
			print("ERROR")
			action = False
		time.sleep(2)
		os.system("cls")
		if charge == 1:
			print(dolphine(debug))
			print(EvilName + " summons dolphin")
			charge -= 1
		if dolphine = 1:
			print(EvilName + " is charging up an attack")
			charge = 1
			dolphine += 1
		else:
			dolphine += 1
			if dolphine = 11:
				dolphine = 1
			if weapon == "banana":
				print(Story3nanner(debug))
				print(EvilName + " uses " + weapon)
				time.sleep(1)
				os.system("cls")
				print(Story3e(debug))
		
		else:
			print("hmm")


