from Screen import *
from Getters import *
from Story1 import *
from Story2 import *
from Story3 import *
import time
import os

def Madlibs(debug = False):
	if debug: print("Welcome to Madlibs debug")

	print(startScreen(debug))
	input()
	os.system("cls")
	number = 1
	menu = False
	menuChoice1 = True
	menuChoice2 = True
	menuChoice3 = True
	while menu == False:
		print(menuScreen(debug))
		choice = getMenuOption(debug)
		os.system("cls")
		if choice == 1:
			menu = True
			if number == 1:
				menuChoice1 = False
			elif number == 2:
				menuChoice2 = False
			elif number == 3:
				menuChoice3 = False
			while menuChoice1 == False:
				number = 1
				print(storySelectScreen1(debug))
				choice = getMenuOption(debug)
				os.system("cls")	
				if choice == 1:
					menuChoice1 = True
					print(Story1(debug))
					input("Press Enter to continue")
					os.system("cls")
					menuChoice2 = False
				elif choice == 101:
					number = 3
					menuChoice3 = False
					menuChoice1 = True
					menu = False
				elif choice == 10:
					menuChoice1 = True
					menu = False
				else:
					menuChoice1 = False
			while menuChoice2 == False:
				number = 2
				print(storySelectScreen2(debug))
				choice = getMenuOption(debug)
				os.system("cls")	
				if choice == 1:
					menuChoice2 = True
					print(Story1(debug))
					input("Press Enter to continue")
					os.system("cls")
					menuChoice2 = False
				if choice == 2:
					menuChoice2 = True
					print(Story2(debug))
					input("Press Enter to continue")
					os.system("cls")
					print("Congratulations, you have unlocked a secret picture")
					time.sleep(1)
					img = DK(debug)
					img.show()
					os.system("cls")
					menuChoice3 = False
				elif choice == 10:
					menuChoice2 = True
					menu = False
				else:
					menuChoice2 = False
			while menuChoice3 == False:
				number = 3
				print(storySelectScreen3(debug))
				choice = getMenuOption(debug)
				os.system("cls")	
				if choice == 1:
					menuChoice2 = True
					print(Story1(debug))
					input("Press Enter to continue")
					os.system("cls")
					menuChoice2 = False
				if choice == 2:
					menuChoice2 = True
					print(Story2(debug))
					input("Press Enter to continue")
					os.system("cls")
					print("Congratulations, you have unlocked a secret picture")
					time.sleep(1)
					img = DK(debug)
					img.show()
					os.system("cls")
					menuChoice3 = False
				if choice == 3:
					menuChoice3 = True
					print(Story3(debug))
					input("Press Enter to continue")
					os.system("cls")
					menuChoice4 = False
				elif choice == 10:
					menuChoice3 = True
					menu = False
				else:
					menuChoice3 = False
		elif choice == 2:
			print("Noice")
		elif choice == 3:
			quit()
	
Madlibs()
