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
	defense = 1
	EvilName = getMadlibOption("Enter a name: ", debug)
	dolphineName = getMadlibOption("Enter another name: ", debug)
	weapon = getWeapon("Enter a weapon: ", debug)
	dolphin = random.randint(1, 10)
	charge = 0
	
	#Music
	
	mixer.init()
	os.system('cls')




	mixer.music.load("Mini Boss.mp3")

	time="00:00"
	wast=""
	def pad(num):
		out = ""
		if num<10:
			out = "0"
		out += str(num)
        
		return out


	while True:
		mixer.music.play()
		t=0
		while mixer.music.get_busy():
			if not t==wast:
				os.system('cls')
				print(time)

			wast=t
			t=mixer.music.get_pos()
			t//=1000
			m = t//60
			s = t%60
			time=pad(m)+":"+pad(s)
	
	os.system("cls")
	print(Story3a(SP, EHP, UHP, debug))
	print(EvilName + " approaches you")
	var = 0
	time.sleep(1)
	action = False
	while action == False:
		if var > 0:
			print(Story3a(SP, EHP, UHP, debug))
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
			print(Story3a(SP, EHP, UHP, debug))
			if EHP <= 0:
				print("ARG, how could I lose")
			time.sleep(2)
			if EHP <= 0:
				os.system("cls")
				print(winScreen(debug))
				break
			os.system("cls")
		elif act.lower() == "d":
				print(Story3d(SP, EHP, UHP, debug))
				defense += 1
				time.sleep(2)
				action = True
		elif act.lower() == "c":
			SP += 3
			if SP > 5:
				SP = 5
			print(Story3c(SP, EHP, UHP, debug))
			time.sleep(2)
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
			print(Story3a(SP, EHP, UHP, debug))
			if EHP <= 0:
				print("ARG, how could I lose")
			time.sleep(2)
			SP = 0
			if EHP <= 0:
				os.system("cls")
				print(winScreen(debug))
				break
		else:
			print("ERROR")
			action = False
		os.system("cls")
		if charge == 1:
			print(dolphine(debug))
			print(EvilName + " summons " + dolphineName + " the dolphin")
			UHP -= round(4/defense)
			charge -= 1
			defense = 1
			time.sleep(2)
			os.system("cls")
			action = False
		elif dolphin == 1:
			print(ZipZamWhamBoomBam(debug))
			print(EvilName + " is charging up an attack")
			charge = 1
			dolphin += 1
			defense = 1
			time.sleep(1)
			os.system("cls")
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
				action = False


