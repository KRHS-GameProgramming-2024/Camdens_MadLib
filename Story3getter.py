from Story3 import *

def Story3a(EHP, UHP, debug = False):
	if debug: print("Story 3a Function")
	if EHP == 8:
		HimHP = "▇▇▇▇▇▇▇▇"
	elif EHP == 7:
		HimHP = "▇▇▇▇▇▇▇▁"
	elif EHP == 6:
		HimHP = "▇▇▇▇▇▁▁"
	elif EHP == 5:
		HimHP = "▇▇▇▇▇▁▁▁"
	elif EHP == 4:
		HimHP = "▇▇▇▇▁▁▁▁"
	elif EHP == 3:
		HimHP = "▇▇▇▁▁▁▁▁"
	elif EHP == 2:
		HimHP = "▇▇▁▁▁▁▁▁"
	elif EHP == 1:
		HimHP = "▇▁▁▁▁▁▁▁"
	if UHP == 8:
		YouHP = "▇▇▇▇▇▇▇▇"
	elif UHP == 7:
		HimHP = "▇▇▇▇▇▇▇▁"
	elif UHP == 6:
		HimHP = "▇▇▇▇▇▁▁"
	elif UHP == 5:
		HimHP = "▇▇▇▇▇▁▁▁"
	elif UHP == 4:
		HimHP = "▇▇▇▇▁▁▁▁"
	elif UHP == 3:
		HimHP = "▇▇▇▁▁▁▁▁"
	elif UHP == 2:
		HimHP = "▇▇▁▁▁▁▁▁"
	elif UHP == 1:
		HimHP = "▇▁▁▁▁▁▁▁"
	
	z =  " ____________________________________ \n"
	z += "| HP:            ___                 |\n"
	z += "|[" + HimHP + "]     /. .\\                |\n"
	z += "|              [  V  ]               |\n"
	z += "|               \\___/                |\n"
	z += "|                /|\\                 |\n"
	z += "|               / | \\                |\n"
	z += "|              /  |  \\               |\n"
	z += "|                 |                  |\n"
	z += "|                 |                  |\n"
	z += "|                / \\                 |\n"
	z += "|               /   \\                |\n"	
	z += "|              /     \\               |\n"
	z += "|   +======+  |||||||||  +======+    |\n"
	z += "|   |ATTACK|   \\\\\\|///   |DEFEND|    |\n"	
	z += "|   +======+     [|]     +======+    |\n"
	z += "|____________________________________|\n"
	z += "| You:                               |\n"
	z += "|   [" + YouHP + "]                       |\n"
	z += "|____________________________________|\n"
	
	return z

def Story3d(EHP, UHP, debug = False):
	if debug: print("Story 3d Function")
	if EHP == 8:
		HimHP = "▇▇▇▇▇▇▇▇"
	elif EHP == 7:
		HimHP = "▇▇▇▇▇▇▇▁"
	elif EHP == 6:
		HimHP = "▇▇▇▇▇▁▁"
	elif EHP == 5:
		HimHP = "▇▇▇▇▇▁▁▁"
	elif EHP == 4:
		HimHP = "▇▇▇▇▁▁▁▁"
	elif EHP == 3:
		HimHP = "▇▇▇▁▁▁▁▁"
	elif EHP == 2:
		HimHP = "▇▇▁▁▁▁▁▁"
	elif EHP == 1:
		HimHP = "▇▁▁▁▁▁▁▁"
	if UHP == 8:
		YouHP = "▇▇▇▇▇▇▇▇"
	elif UHP == 7:
		HimHP = "▇▇▇▇▇▇▇▁"
	elif UHP == 6:
		HimHP = "▇▇▇▇▇▁▁"
	elif UHP == 5:
		HimHP = "▇▇▇▇▇▁▁▁"
	elif UHP == 4:
		HimHP = "▇▇▇▇▁▁▁▁"
	elif UHP == 3:
		HimHP = "▇▇▇▁▁▁▁▁"
	elif UHP == 2:
		HimHP = "▇▇▁▁▁▁▁▁"
	elif UHP == 1:
		HimHP = "▇▁▁▁▁▁▁▁"
		
	z =  " ____________________________________ \n"
	z += "| HP:            ___                 |\n"
	z += "|[" + HimHP + "]     /. .\\                |\n"
	z += "|              [  V  ]               |\n"
	z += "|               \\___/                |\n"
	z += "|                /|\\                 |\n"
	z += "|               / | \\                |\n"
	z += "|              /  |  \\               |\n"
	z += "|                 |                  |\n"
	z += "|                 |                  |\n"
	z += "|                / \\                 |\n"
	z += "|               /   \\                |\n"	
	z += "|              /     \\               |\n"
	z += "|   +======+  |||||||||  +======+    |\n"
	z += "|   |ATTACK|   \\\\\\|///   |DEFEND|    |\n"	
	z += "|   +======+     [|]     +======+    |\n"
	z += "|____________________________________|\n"
	z += "| You:                               |\n"
	z += "|   [" + YouHP + "]          defense⬆️    |\n"
	z += "|____________________________________|\n"
	
	return z

def Story3acttack(debug = False):
	if debug: print("Story 3 attack Function")
	
		
	z =  " ____________________________________ \n"
	z += "|                ___        .-       |\n"
	z += "|               /. .\\      //        |\n"
	z += "|              [  ^  ]   ,/:         |\n"
	z += "|               \\___/   /[}          |\n"
	z += "|                /|\\  /|/            |\n"
	z += "|               / |,/'/'             |\n"
	z += "|              / ,//'\\               |\n"
	z += "|               ;/}                  |\n"
	z += "|             ,// |                  |\n"
	z += "|           ,/;' / \\                 |\n"
	z += "|         ,//'  /   \\                |\n"	
	z += "|              /     \\               |\n"
	z += "|             |||||||||              |\n"
	z += "|              \\\\\\|///               |\n"	
	z += "|                [|]                 |\n"
	z += "|____________________________________|\n"
	
	return z

def Story3nanner(debug = False):
	if debug: print("Story 3 banana Function")
	z =  " ____________________________________ \n"
	z += "|                ___                 |\n"
	z += "|               /. .\\                |\n"
	z += "|              [  V  ]               |\n"
	z += "|               \\___/                |\n"
	z += "|                /|\\                 |\n"
	z += "|               / | \\  _,---._       |\n"
	z += "|              /  |  \\; ,---._;O     |\n"
	z += "|                 |   |'             |\n"
	z += "|                 |                  |\n"
	z += "|                / \\                 |\n"
	z += "|               /   \\                |\n"	
	z += "|              /     \\               |\n"
	z += "|             |||||||||              |\n"
	z += "|              \\\\\\|///               |\n"	
	z += "|                [|]                 |\n"
	z += "|____________________________________|\n"
	
	return z

def dolphine(debug = False):
	if debug: print("Story 3 dolphine Function")
	z =  " ____________________________________ \n"
	z += "|        _______                     |\n"
	z += "|   ____/        \\_                  |\n" 
	z += "|  \\        o\     \\____             |\n"
	z += "|   \\               ____)            |\n" 
	z += "|   /            __/                 |\n" 
	z += "|   |  /    /   /                    |\n"
	z += "|   |  |   /   /|                    |\n"
	z += "|   \\   \\_/   /_/                ,/',|\n"
	z += "|    \\       /              ,~;{/'`~ |\n"
	z += "|     \\     /             ;']/~-‘’-< |\n"
	z += "|     /     \\         ,</(/[.';`,~‘’;|\n"
	z += "|~~~ / _/ \\_ \\ ~~;~’’`~;~{~’;~~/,`  `|\n"
	z += "|   /_/     \\_\\  /=``,’;’^-~;’’  {,’/|\n"
	z += "|                ‘’’;;-’;’;;;/’``;’. |\n"
	z += "|                     ‘      ‘’ ‘    |\n" 
	z += "|____________________________________|\n"
	
	return z

def ZipZamWhamBoomBam(debug = False):
	if debug: print("Story 3 dolphine Function")
	z =  " ____________________________________ \n"
	z += "|             _/ ___ \\_              |\n"
	z += "|           __\\ /. .\\ /__            |\n"
	z += "|         __\\  [  V  ]  /__          |\n"
	z += "|         \\     \\___/     /          |\n"
	z += "|          \\     /|\\     /           |\n"
	z += "|         __\\   / | \\   /__          |\n"
	z += "|         \\    /  |  \\    /          |\n"
	z += "|          \\      |      /           |\n"
	z += "|           \\     |     /            |\n"
	z += "|           _\\   / \\   /_            |\n"
	z += "|           \\   /   \\   /            |\n"	
	z += "|            \\ /     \\ /             |\n"
	z += "|             |||||||||              |\n"
	z += "|              \\\\\\|///               |\n"	
	z += "|                [|]                 |\n"
	z += "|____________________________________|\n"	
	
	return z
