from Getters import *
from Screen import *
from Story3getter import *
import os
import time
import random


def Story3(debug = False):
	if debug: print("Story 3 Function")
	
	SP = 0
	EHP = 8
	UHP = 8
	power = 1
	notice = 0
	defense = 1
	EvilName = getMadlibOption("Enter a name: ", debug)
	dolphineName = getMadlibOption("Enter another name: ", debug)
	weapon = getWeapon("Enter a generic weapon: ", debug)
	dolphin = random.randint(1, 6)
	charge = 0
	os.system("cls")
	print(Story3a(power, SP, EHP, UHP, debug))
	print(EvilName + " approaches you")
	var = 0
	time.sleep(1)
	action = False
	while action == False:
		if var > 0:
			print(Story3a(power, SP, EHP, UHP, debug))
			if UHP <= 0:
				os.system("cls")
				print(loseScreen(debug))
				break
		var += 1
		act = input("Attack, Defend, Charge, or Use Special, A/D/C/S: ")
		os.system("cls")	
		if act.lower() == "a":
			print(Story3acttack(debug))
			time.sleep(.5)
			SP += 1
			if SP > 5:
				SP = 5
			EHP -= 1
			os.system("cls")
			if power == 1 and EHP <= 5:
				power = 2
				notice = 1
			if power == 2 and EHP <= 2:
				power = 3
				notice = 2
			print(Story3a(power, SP, EHP, UHP, debug))
			if notice == 1:
				print(EvilName + " is getting serious")
				notice = 0
			if notice == 2:
				print(EvilName + " is getting mad")
				notice = 0
			if EHP <= 0:
				print("ARG, how could I lose")
				time.sleep(2)
				print("No, I'm not giving up just yet")
				for x in range(8):
					print(Story3a(power, SP, EHP, UHP, debug))
					time.sleep(.1)
			time.sleep(2)
			if EHP <= 0:
				os.system("cls")
				print(winScreen(debug))
				break
			action = True
			os.system("cls")
		elif act.lower() == "d":
			SP += 1
			if SP > 5:
				SP = 5
			print(Story3d(power, SP, EHP, UHP, debug))
			defense += 1
			time.sleep(2)
			action = True
		elif act.lower() == "c":
			SP += 3
			if SP > 5:
				SP = 5
			print(Story3c(power, SP, EHP, UHP, debug))
			time.sleep(2)
			action = True
		elif act.lower() == "s":
			Switch = 0
			for x in range(SP):
				if Switch == 0:
					print(Story3acttack(debug))
					time.sleep(.5)
					os.system("cls")
					Switch += 1
				elif Switch == 1:
					print(Story3acttackB(debug))
					time.sleep(.5)
					os.system("cls")
					Switch -= 1
			EHP -= SP
			SP = 0
			if power == 1 and EHP <= 5:
				power = 2
				notice = 1
			if power == 2 and EHP <= 2:
				power = 3
				notice = 2
			print(Story3a(power, SP, EHP, UHP, debug))
			if notice == 1:
				print(EvilName + " is getting serious")
				notice = 0
			if notice == 2:
				print(EvilName + " is getting mad")
				notice = 0
			if EHP <= 0:
				print("ARG, how could I lose")
				time.sleep(2)
				print("No, I'm not giving up just yet")
				time.sleep(2)
				for x in range(8):
					print(Story3a(power, SP, EHP, UHP, debug))
					EHP += 1
					time.sleep(.1)
					os.system("cls")
			time.sleep(2)
			if EHP <= 0:
				os.system("cls")
				print(winScreen(debug))
				break
			action = True
		else:
			print("ERROR")
			time.sleep(1)
			action = False
		os.system("cls")
		if action == True:
			if charge == 1:
				print(dolphine(debug))
				print(EvilName + " summons " + dolphineName + " the dolphin")
				UHP -= round(6/defense)
				charge -= 1
				defense = 1
				time.sleep(2)
				os.system("cls")
				action = False
			elif dolphin == 1:
				print(ZipZamWhamBoomBam(power, debug))
				print(EvilName + " is charging up an attack")
				charge = 1
				dolphin += 1
				defense = 1
				time.sleep(1)
				os.system("cls")
				action = False
			else:
				dolphin += 1
				if dolphin == 6:
					dolphin = 1
				if weapon == "banana":
					print(Story3nanner(power, debug))
					print(EvilName + " uses " + weapon)
					time.sleep(1)
					os.system("cls")
					UHP -= round(power/defense)
					defense = 1
					action = False
				elif weapon == "pumpkin":
					print(Story3pumpkin(debug))
					print(EvilName + " uses " + weapon)
					time.sleep(1)
					os.system("cls")
					UHP -= round(power/defense)
					defense = 1
					action = False
				elif weapon == "cucumber":
					print(Story3cuke(power, debug))
					print(EvilName + " uses " + weapon)
					time.sleep(1)
					os.system("cls")
					UHP -= round(power/defense)
					defense = 1
					action = False
				elif weapon == "banjo":
					print(Story3banjo(power, debug))
					print(EvilName + " uses " + weapon)
					time.sleep(1)
					os.system("cls")
					UHP -= round(power/defense)
					defense = 1
					action = False
				else:
					print("What?")
					time.sleep(2)

