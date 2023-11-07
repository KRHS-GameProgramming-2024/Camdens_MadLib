from Getters import *
from Screen import *
from Story3getter import *
import os
import time
import random

def Story3(debug = False):
	if debug: print("Story 3 Function")
	
	EHP = 8
	UHP = 8
	defense = 1
	EvilName = getMadlibOption("Enter a name: ", debug)
	weapon = getWeapon("Enter a weapon: ", debug)
	dolphin = random.randint(1, 10)
	charge = 0
	
	os.system("cls")
	print(Story3a(EHP, UHP, debug))
	print(EvilName + " approaches you")
	var = 0
	time.sleep(1)
	action = False
	while action == False:
		if var > 0:
			print(Story3a(EHP, UHP, debug))
		var += 1
		act = input("Attack or Defend, A/D: ")
		os.system("cls")	
		if act.lower() == "a":
			print(Story3acttack(debug))
			EHP -= 1
			if EHP <= 0:
				os.system("cls")
				print(winScreen(debug))
				break
			print(Story3a(EHP, UHP, debug))
			time.sleep(.2)
			os.system("cls")
		elif act.lower() == "d":
				print(Story3d(EHP, UHP, debug))
				defense += 1
				time.sleep(2)
				action = True
		else:
			print("ERROR")
			action = False
		os.system("cls")
		if charge == 1:
			print(dolphine(debug))
			print(EvilName + " summons dolphin")
			UHP -= round(4/defense)
			charge -= 1
			defense = 1
			if UHP <= 0:
				os.system("cls")
				print(loseScreen(debug))
				break
			time.sleep(1)
			action = False
		elif dolphin == 1:
			print(ZipZamWhamBoomBam(debug))
			print(EvilName + " is charging up an attack")
			charge = 1
			dolphin += 1
			defense = 1
			time.sleep(1)
			action = False
		else:
			dolphin += 1
			if dolphin == 11:
				dolphin = 1
			if weapon == "banana":
				print(Story3nanner(debug))
				print(EvilName + " uses " + weapon)
				time.sleep(1)
				os.system("cls")
				UHP -= round(1/defense)
				defense = 1
				if UHP <= 0:
					os.system("cls")
					print(loseScreen(debug))
					break
				action = False



