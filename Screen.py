from PIL import Image
def startScreen(debug = False):
	if debug: print("Welcome to start screen debug")

	z =  " ____________________________________ \n"
	z += "|                                    |\n"
	z += "|                                    |\n"
	z += "|           M           s            |\n"
	z += "|             a       b              |\n"
	z += "|               d   i                |\n"
	z += "|                 l                  |\n"
	z += "|                                    |\n"
	z += "|                                    |\n"
	z += "|            Press Enter             |\n"
	z += "|                                    |\n"
	z += "|                                    |\n"
	z += "|                         By         |\n"
	z += "|                         Camden     |\n"
	z += "|                         Blasingame |\n"
	z += "|____________________________________|\n"
	
	return z

def menuScreen(debug = False):
	if debug: print("Welcome to menu screen debug")

	z =  " ____________________________________ \n"
	z += "|                                    |\n"
	z += "| Menu Screen:                       |\n"
	z += "|                                    |\n"
	z += "|                                    |\n"
	z += "|             Story Mode             |\n"
	z += "|              press(1)              |\n"
	z += "|                                    |\n"
	z += "|           2 Player Mode            |\n"
	z += "|              press(2)              |\n"
	z += "|                                    |\n"
	z += "|                Quit                |\n"
	z += "|              press(3)              |\n"
	z += "|                                    |\n"	
	z += "|                                    |\n"	
	z += "|____________________________________|\n"
	
	return z	

def storySelectScreen1(debug = False):
	if debug: print("Welcome to story select screen debug")

	z =  " ____________________________________ \n"
	z += "|    _                               |\n"
	z += "| <---' Press B                      |\n"
	z += "|                                    |\n"
	z += "|  _____    _____    _____    _____  |\n"
	z += "| |     |  |     |  |     |  |     | |\n"
	z += "| |  1  |  |     |  |     |  |     | |\n"
	z += "| |_____|  |_____|  |_____|  |_____| |\n"	
	z += "|                                    |\n"
	z += "|  _____    _____    _____    _____  |\n"
	z += "| |     |  |     |  |     |  |     | |\n"
	z += "| |     |  |     |  |     |  |     | |\n"
	z += "| |_____|  |_____|  |_____|  |_____| |\n"
	z += "|                                    |\n"
	z += "|           Select a Level           |\n"	
	z += "|____________________________________|\n"
	
	return z
	
def storySelectScreen2(debug = False):
	if debug: print("Welcome to story select screen debug")

	z =  " ____________________________________ \n"
	z += "|    _                               |\n"
	z += "| <---' Press B                      |\n"
	z += "|                                    |\n"
	z += "|  _____    _____    _____    _____  |\n"
	z += "| |     |  |     |  |     |  |     | |\n"
	z += "| |  1  |  |  2  |  |     |  |     | |\n"
	z += "| |_____|  |_____|  |_____|  |_____| |\n"	
	z += "|                                    |\n"
	z += "|  _____    _____    _____    _____  |\n"
	z += "| |     |  |     |  |     |  |     | |\n"
	z += "| |     |  |     |  |     |  |     | |\n"
	z += "| |_____|  |_____|  |_____|  |_____| |\n"
	z += "|                                    |\n"
	z += "|           Select a Level           |\n"	
	z += "|____________________________________|\n"
	
	return z
	
def storySelectScreen3(debug = False):
	if debug: print("Welcome to story select screen debug")

	z =  " ____________________________________ \n"
	z += "|    _                               |\n"
	z += "| <---' Press B                      |\n"
	z += "|                                    |\n"
	z += "|  _____    _____    _____    _____  |\n"
	z += "| |     |  |     |  |     |  |     | |\n"
	z += "| |  1  |  |  2  |  |  3  |  |     | |\n"
	z += "| |_____|  |_____|  |_____|  |_____| |\n"	
	z += "|                                    |\n"
	z += "|  _____    _____    _____    _____  |\n"
	z += "| |     |  |     |  |     |  |     | |\n"
	z += "| |     |  |     |  |     |  |     | |\n"
	z += "| |_____|  |_____|  |_____|  |_____| |\n"
	z += "|                                    |\n"
	z += "|           Select a Level           |\n"	
	z += "|____________________________________|\n"
	
	return z
	
def winScreen(debug = False):
	if debug: print("Welcome to win screen debug")

	z =  " ____________________________________ \n"
	z += "| _       _                          |\n"
	z += "| \\\\     //    ____       _    _     |\n"
	z += "|  \\\\   //    /    \\     | |  | |    |\n"
	z += "|   \\\\_//    /  __  \\    | |  | |    |\n"
	z += "|    | |    |  |__|  |   | |  | |    |\n"
	z += "|    | |     \\      /    | |__| |    |\n"
	z += "|    |_|      \\____/     \\______/    |\n"	
	z += "|                                    |\n"
	z += "|  _       _     ____     _          |\n"
	z += "| | |     | |   /    \\   | |___      |\n"
	z += "| \\ \\  _  / /  /  __  \\  |  __ \\     |\n"
	z += "|  \\ \\/ \/ /  |  |__|  | | |  \\ |    |\n"
	z += "|   |  |  |    \\      /  | |  | |    |\n"
	z += "|    \\/ \\/      \\____/   |_|  |_|    |\n"	
	z += "|____________________________________|\n"
	
	return z
	
def loseScreen(debug = False):
	if debug: print("Welcome to death screen debug")

	z =  " ____________________________________ \n"
	z += "| _       _                          |\n"
	z += "| \\\\     //    ____       _    _     |\n"
	z += "|  \\\\   //    /    \\     | |  | |    |\n"
	z += "|   \\\\_//    /  __  \\    | |  | |    |\n"
	z += "|    | |    |  |__|  |   | |  | |    |\n"
	z += "|    | |     \\      /    | |__| |    |\n"
	z += "|    |_|      \\____/     \\______/    |\n"	
	z += "|                                    |\n"
	z += "|   ____     _    ____    ____       |\n"
	z += "|  |  _ \\   |_|  |  __|  |  _ \\      |\n"
	z += "|  | | \\ |   _   | |__   | | \\ |     |\n"
	z += "|  | | | |  | |  |  __|  | | | |     |\n"
	z += "|  | |_/ |  | |  | |__   | |_/ |     |\n"
	z += "|  |____/   |_|  |____|  |____/      |\n"	
	z += "|____________________________________|\n"
	
	return z

def DK(debug = False):
	if debug: print("Welcome to DK screen debug")
	
	file = "C://Users/Student/Documents/Camden's Folder/2023-09-08 08.37.22 www.youtube.com 542b04b57db5.png"
	img = Image.open(file)
	
	return img
