from Getters import *
from Screen import *
from Story3getter import *
import os
import time

def Story3(debug = False):
	if debug: print("Story 3 Function")
	
	print(Story3a(debug))
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
	


