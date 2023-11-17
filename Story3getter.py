from Story3 import *

def Story3a(power, SP, EHP, UHP, debug = False):
	if debug: print("Story 3a Function")
	if power == 1:
		mouth = "V"
	if power == 2:
		mouth = "-"
	if power == 3:
		mouth = "^"
	if SP == 0:
		FP = " _____ "
	elif SP == 1:
		FP = " ✪____ "
	elif SP == 2:
		FP = " ✪✪___ "
	elif SP == 3:
		FP = " ✪✪✪__ "
	elif SP == 4:
		FP = " ✪✪✪✪_ "
	elif SP == 5:
		FP = " ✪✪✪✪✪ "
	if EHP == 8:
		HimHP = "▇▇▇▇▇▇▇▇"
	elif EHP == 7:
		HimHP = "▇▇▇▇▇▇▇▁"
	elif EHP == 6:
		HimHP = "▇▇▇▇▇▇▁▁"
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
	elif EHP <= 0:
		HimHP = "▁▁▁▁▁▁▁▁"
	if UHP == 8:
		YouHP = "▇▇▇▇▇▇▇▇"
	elif UHP == 7:
		YouHP = "▇▇▇▇▇▇▇▁"
	elif UHP == 6:
		YouHP = "▇▇▇▇▇▇▁▁"
	elif UHP == 5:
		YouHP = "▇▇▇▇▇▁▁▁"
	elif UHP == 4:
		YouHP = "▇▇▇▇▁▁▁▁"
	elif UHP == 3:
		YouHP = "▇▇▇▁▁▁▁▁"
	elif UHP == 2:
		YouHP = "▇▇▁▁▁▁▁▁"
	elif UHP == 1:
		YouHP = "▇▁▁▁▁▁▁▁"
	elif UHP <= 0:
		YouHP = "▁▁▁▁▁▁▁▁"
	
	z =  " ____________________________________ \n"
	z += "| HP:            ___                 |\n"
	z += "|[" + HimHP + "]     /. .\\                |\n"
	z += "|              [  " + mouth + "  ]               |\n"
	z += "|               \\___/                |\n"
	z += "|                /|\\                 |\n"
	z += "|               / | \\                |\n"
	z += "|              /  |  \\    +=======+  |\n"
	z += "| +======+        |       |Special|  |\n"
	z += "| |CHARGE|        |       |  Move |  |\n"
	z += "| +======+       / \\      |" + FP + "|  |\n"
	z += "|               /   \\     +=======+  |\n"	
	z += "|              /     \\               |\n"
	z += "|   +======+  |||||||||  +======+    |\n"
	z += "|   |ATTACK|   \\\\\\|///   |DEFEND|    |\n"	
	z += "|   +======+     [|]     +======+    |\n"
	z += "|____________________________________|\n"
	z += "| You:                               |\n"
	z += "|   [" + YouHP + "]                       |\n"
	z += "|____________________________________|\n"
	
	return z

def Story3d(power, SP, EHP, UHP, debug = False):
	if debug: print("Story 3d Function")
	if power == 1:
		mouth = "V"
	if power == 2:
		mouth = "-"
	if power == 3:
		mouth = "^"
	if SP == 0:
		FP = " _____ "
	elif SP == 1:
		FP = " ✪____ "
	elif SP == 2:
		FP = " ✪✪___ "
	elif SP == 3:
		FP = " ✪✪✪__ "
	elif SP == 4:
		FP = " ✪✪✪✪_ "
	elif SP == 5:
		FP = " ✪✪✪✪✪ "
	if EHP == 8:
		HimHP = "▇▇▇▇▇▇▇▇"
	elif EHP == 7:
		HimHP = "▇▇▇▇▇▇▇▁"
	elif EHP == 6:
		HimHP = "▇▇▇▇▇▇▁▁"
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
	elif EHP <= 0:
		HimHP = "▁▁▁▁▁▁▁▁"
	if UHP == 8:
		YouHP = "▇▇▇▇▇▇▇▇"
	elif UHP == 7:
		YouHP = "▇▇▇▇▇▇▇▁"
	elif UHP == 6:
		YouHP = "▇▇▇▇▇▇▁▁"
	elif UHP == 5:
		YouHP = "▇▇▇▇▇▁▁▁"
	elif UHP == 4:
		YouHP = "▇▇▇▇▁▁▁▁"
	elif UHP == 3:
		YouHP = "▇▇▇▁▁▁▁▁"
	elif UHP == 2:
		YouHP = "▇▇▁▁▁▁▁▁"
	elif UHP == 1:
		YouHP = "▇▁▁▁▁▁▁▁"
	elif EHP <= 0:
		YouHP = "▁▁▁▁▁▁▁▁"
		
	z =  " ____________________________________ \n"
	z += "| HP:            ___                 |\n"
	z += "|[" + HimHP + "]     /. .\\                |\n"
	z += "|              [  " + mouth + "  ]               |\n"
	z += "|               \\___/                |\n"
	z += "|                /|\\                 |\n"
	z += "|               / | \\                |\n"
	z += "|              /  |  \\    +=======+  |\n"
	z += "| +======+        |       |Special|  |\n"
	z += "| |CHARGE|        |       |  Move |  |\n"
	z += "| +======+       / \\      |" + FP + "|  |\n"
	z += "|               /   \\     +=======+  |\n"	
	z += "|              /     \\               |\n"
	z += "|   +======+  |||||||||  +======+    |\n"
	z += "|   |ATTACK|   \\\\\\|///   |DEFEND|    |\n"	
	z += "|   +======+     [|]     +======+    |\n"
	z += "|____________________________________|\n"
	z += "| You:                               |\n"
	z += "|   [" + YouHP + "]          defense⬆️    |\n"
	z += "|____________________________________|\n"
	
	return z

def Story3c(power, SP, EHP, UHP, debug = False):
	if debug: print("Story 3d Function")
	if power == 1:
		mouth = "V"
	if power == 2:
		mouth = "-"
	if power == 3:
		mouth = "^"
	if SP == 0:
		FP = " _____ "
	elif SP == 1:
		FP = " ✪____ "
	elif SP == 2:
		FP = " ✪✪___ "
	elif SP == 3:
		FP = " ✪✪✪__ "
	elif SP == 4:
		FP = " ✪✪✪✪_ "
	elif SP == 5:
		FP = " ✪✪✪✪✪ "
	if EHP == 8:
		HimHP = "▇▇▇▇▇▇▇▇"
	elif EHP == 7:
		HimHP = "▇▇▇▇▇▇▇▁"
	elif EHP == 6:
		HimHP = "▇▇▇▇▇▇▁▁"
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
	elif EHP <= 0:
		HimHP = "▁▁▁▁▁▁▁▁"
	if UHP == 8:
		YouHP = "▇▇▇▇▇▇▇▇"
	elif UHP == 7:
		YouHP = "▇▇▇▇▇▇▇▁"
	elif UHP == 6:
		YouHP = "▇▇▇▇▇▇▁▁"
	elif UHP == 5:
		YouHP = "▇▇▇▇▇▁▁▁"
	elif UHP == 4:
		YouHP = "▇▇▇▇▁▁▁▁"
	elif UHP == 3:
		YouHP = "▇▇▇▁▁▁▁▁"
	elif UHP == 2:
		YouHP = "▇▇▁▁▁▁▁▁"
	elif UHP == 1:
		YouHP = "▇▁▁▁▁▁▁▁"
	elif UHP <= 0:
		YouHP = "▁▁▁▁▁▁▁▁"
		
	z =  " ____________________________________ \n"
	z += "| HP:            ___                 |\n"
	z += "|[" + HimHP + "]     /. .\\                |\n"
	z += "|              [  " + mouth + "  ]               |\n"
	z += "|               \\___/                |\n"
	z += "|                /|\\                 |\n"
	z += "|               / | \\                |\n"
	z += "|              /  |  \\    +=======+  |\n"
	z += "| +======+        |       |Special|  |\n"
	z += "| |CHARGE|        |       |  Move |  |\n"
	z += "| +======+       / \\      |" + FP + "|  |\n"
	z += "|               /   \\     +=======+  |\n"	
	z += "|              /     \\               |\n"
	z += "|   +======+  |||||||||  +======+    |\n"
	z += "|   |ATTACK|   \\\\\\|///   |DEFEND|    |\n"	
	z += "|   +======+     [|]     +======+    |\n"
	z += "|____________________________________|\n"
	z += "| You:                               |\n"
	z += "|   [" + YouHP + "]           charge⬆️    |\n"
	z += "|____________________________________|\n"
	
	return z
def Story3acttack(debug = False):
	if debug: print("Story 3 attack Function")
	
	z =  " ____________________________________ \n"
	z += "|                ___        .-       |\n"
	z += "|               /o o\\      //        |\n"
	z += "|              [  0  ]   ,/:         |\n"
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
	
def Story3acttackB(debug = False):
	if debug: print("Story 3 attack Function")
	
	z =  " ____________________________________ \n"
	z += "|       -.       ___                 |\n"
	z += "|         \\\\    /o o\\                |\n"
	z += "|          :\\. [  0  ]               |\n"
	z += "|           {]\\ \\___/                |\n"
	z += "|            \\|\\ /|\\                 |\n"
	z += "|             '\\'\\. \\                |\n"
	z += "|              / '\\\\ \\               |\n"
	z += "|                 |'\\.               |\n"
	z += "|                 |  \\\\.             |\n"
	z += "|                / \\  ';\\.           |\n"
	z += "|               /   \\   '\\\\.         |\n"	
	z += "|              /     \\               |\n"
	z += "|             |||||||||              |\n"
	z += "|              \\\\\\|///               |\n"	
	z += "|                [|]                 |\n"
	z += "|____________________________________|\n"
	
	return z

def Story3nanner(power, debug = False):
	if debug: print("Story 3 banana Function")
	if power == 1:
		mouth = "V"
	if power == 2:
		mouth = "-"
	if power == 3:
		mouth = "^"
	z =  " ____________________________________ \n"
	z += "|                ___                 |\n"
	z += "|               /. .\\                |\n"
	z += "|              [  " + mouth + "  ]               |\n"
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

def Story3cuke(power, debug = False):
	if debug: print("Story 3 cucumber Function")
	if power == 1:
		mouth = "V"
	if power == 2:
		mouth = "-"
	if power == 3:
		mouth = "^"
	z =  " ____________________________________ \n"
	z += "|                ___                 |\n"
	z += "|               /. .\\      _         |\n"
	z += "|              [  " + mouth + "  ]    //         |\n"
	z += "|               \\___/    //          |\n"
	z += "|                /|\\    //           |\n"
	z += "|               / | \\  //            |\n"
	z += "|              /  |  \\//             |\n"
	z += "|                 |  //              |\n"
	z += "|                 |  '               |\n"
	z += "|                / \\                 |\n"
	z += "|               /   \\                |\n"	
	z += "|              /     \\               |\n"
	z += "|             |||||||||              |\n"
	z += "|              \\\\\\|///               |\n"	
	z += "|                [|]                 |\n"
	z += "|____________________________________|\n"
	
	return z

def Story3pumpkin(debug = False):
	if debug: print("Story 3 pumpkin Function")
	z = " ___________________________________ \n"
	z += "|             ___         __	    |\n"
	z += "|            /. .\\        \\ \\       |\n"
	z += "|           [ ~.~ ]    ___|__|___   |\n" 
	z += "|       ✊   \\___/    // /    \\ \\\\  |\n"
	z += "|        \\    /|\\     || |     | || |\n"
	z += "|         \\  / | \\    || |     | || |\n"
	z += "|          \\/  |  \\___\\\\ |     | || |\n"
	z += "|	       |       \\\\_\\___/_//  |\n"
	z += "|	       |                    |\n"  
	z += "|	      / \\                   |\n"
	z += "|            /   \\                  |\n"
	z += "|           /     \\                 |\n"
	z += "|          |||||||||                |\n"
	z += "|           \\\\\\|///                 |\n"
	z += "|             [|]                   |\n"
	z += "|___________________________________|\n"
	
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

def ZipZamWhamBoomBam(power, debug = False):
	if debug: print("Story 3 dolphine Function")
	if power == 1:
		mouth = "V"
	if power == 2:
		mouth = "-"
	if power == 3:
		mouth = "^"
	z =  " ____________________________________ \n"
	z += "|             _/ ___ \\_              |\n"
	z += "|           __\\ /. .\\ /__            |\n"
	z += "|         __\\  [  " + mouth + "  ]  /__          |\n"
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
def Story3banjo(power, debug = False):
	if debug: print("Story 3 banjo Function")
	if power == 1:
		mouth = "V"
	if power == 2:
		mouth = "-"
	if power == 3:
		mouth = "^"	
	z =  " ____________________________________ \n"
	z += "|                ___                 |\n"
	z += "|               /. .\\                |\n"
	z += "|              [  " + mouth + "  ]'{}'           |\n"
	z += "|               \\___/'{}'            |\n"
	z += "|                /| \\//              |\n"
	z += "|               / | //\\              |\n"
	z += "|              /  |//__\\             |\n"
	z += "|                _//                 |\n"
	z += "|               /   \\                |\n"
	z += "|              | /// |               |\n"
	z += "|               \\___/                |\n"
	z += "|               /   \\                |\n"
	z += "|              /     \\               |\n"
	z += "|             |||||||||              |\n"
	z += "|              \\\\\\|///               |\n"
	z += "|                [|]                 |\n"
	z += "|____________________________________|\n"
	
	return z

def Story3mad(debug = False):
	if debug: print("Story 3 mad Function")
	
	z =  " ____________________________________ \n"
	z += "|                                    |\n"
	z += "|                                    |\n"
	z += "|           ___________              |\n"
	z += "|          /           \\             |\n"
	z += "|         /   -.   .-   \\            |\n"
	z += "|        /    0 \\ / 0    \\           |\n"
	z += "|       /                 \\          |\n"
	z += "|     .-      .-----.      -.        |\n"
	z += "|     |      //'''''\\\\      |        |\n"
	z += "|     '-    //       \\\\    -'        |\n"
	z += "|       \\  |/         \\|  /          |\n"
	z += "|        \\               /           |\n"
	z += "|         \\             /            |\n"
	z += "|          \\___________/             |\n"
	z += "|                                    |\n"
	z += "|                                    |\n"
	z += "|____________________________________|\n"
	
	return z
