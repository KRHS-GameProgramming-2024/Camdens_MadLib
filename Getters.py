import time
def getMenuOption(debug = False):
	if debug: print("getMenuOption Functions")
	
	goodInput = False
	
	while not goodInput:
		option = input()
	
		if option == "1":
			option = 1
			goodInput = True			
		elif option == "2":
			option = 2	
			goodInput = True		
		elif option == "3":			
			option = 3
			goodInput = True
		elif option == "B":			
			option = 10
			goodInput = True
		elif option == "Unlock All":			
			option = 101
			goodInput = True
		else:
			print("Hmmm Try Again")
			
	return option

def getMadlibOption(prompt, debug = False):
	if debug: print("getMadlibOption Functions")
	
	goodInput = False
	
	wordCheck = ""
	
	
	
	while not goodInput:
		word = input(prompt)
		for i in word:
			if not i == " ":
				wordCheck += i
		goodInput = True
		if isSwear(wordCheck):
			goodInput = False
			print("No")
			time.sleep(10000)
			quit()
			
	
			
	return word	
	
def getWeapon(prompt, debug = False):
	if debug: print("getMadlibOptionZeldaMonster Functions")
	
	goodInput = False	
	
	
	
	while not goodInput:
		word = input(prompt)  
		if isWeapon(word):
			if word.lower() == "gun":
				word = "banana"
			elif word.lower() == "sword":	
				word = "cucumber"
			goodInput = True
		else:
			print("ERROR")
			goodInput = False
	
			
	return word	
	
def isWeapon(word, debug = False):
	if debug: print("Weapon Functions")
	
	if word.lower() == "gun":
		word = "banana"
		print("Due to school protocols your response has been change to " + word + ".")
		time.sleep(2)		
		return True
	elif word.lower() == "sword":		
		word = "cucumber"
		print("Due to school protocols your response has been change to " + word + ".")	
		return True
	else:
		return False		


def isSwear(wordCheck, debug = False):
	if debug: print("isSwear Functions")
	
	if wordCheck.lower() in SwearList:
		return True
	else:
		return False

SwearList = [
"arse",
"arsehead",
"arsehole",
"ass",
"asshole",
"bastard",
"bitch",
"bloody",
"bollocks",
"brotherfucker",
"bugger",
"bullshit",
"child-fucker",
"cock",
"cocksucker",
"crap",
"cunt",
"damn",
"damn it",
"dick",
"dickhead",
"dyke",
"fatherfucker",
"frigger",
"fuck",
"goddamn",
"godsdamn",
"holy shit",
"horseshit",
"in shit",
"kike",
"motherfucker",
"nigga",
"nigra",
"pigfucker",
"piss",
"prick",
"pussy",
"shit",
"shit ass",
"shite",
"sisterfucker",
"slut",
"son of a whore",
"son of a bitch",
"spastic",
"turd",
"twat",
"wanker"]

def getMadlibOptionNumber(prompt, range1, range2, debug = False):
	if debug: print("getMadlibOptionNumber Functions")
	
	goodInput = False	
	
	
	
	while not goodInput:
		word = input(prompt)
		if isNumber(word, range1, range2):
			goodInput = True
		else:
			goodInput = False
	
			
	return word
	

def isNumber(word, range1, range2, debug = False):
	if debug: print("isNumber Functions")
	try:
		value = int(word)
	except:
		return False
	if value >= range1 and value <= range2:
		return True
	else:
		return False
		

def getMadlibOptionZeldaMonster(prompt, debug = False):
	if debug: print("getMadlibOptionZeldaMonster Functions")
	
	goodInput = False	
	
	
	
	while not goodInput:
		word = input(prompt)
		if isMonster(word):
			goodInput = True
		else:
			goodInput = False
	
			
	return word
	
def isMonster(word, debug = False):
	if debug: print("isMonster Functions")
	
	if word.lower() in MonsterList:
		return True
	else:
		return False
		
MonsterList = [ "Ache",
"Acheman",
"Acro-Bandit",
"Aeralfos",
"Ampilus",
"Anti-Fairy",
"Anubis",
"Aracha",
"Arm Mimic",
"Armored Train",
"Armos",
"Armos Knight",
"Armos Titan",
"Aru Lowder",
"Arwing",
"Baba Serpent",
"Babusu",
"Baby Dodongo",
"Baby Gohma",
"Bad Bat",
"Bago Bago",
"Ball & Chain Trooper",
"Bari",
"Bawb",
"Beamos",
"Bee",
"Beetle",
"Bellum Blob",
"Big Baba",
"Big Blin",
"Big Deku Baba",
"Big Poe",
"Big Skulltula",
"Bigocto",
"Bio Deku Baba",
"Bio-Electric Cube",
"Biri",
"Bit",
"Blade Trap",
"Blastworm",
"Blob",
"Blooper",
"Blue Bubble",
"Blue ChuChu",
"Bob-omb",
"Boe",
"Boko Baba",
"Bokoblin",
"Bomb Fish",
"Bombarossa",
"Bombite",
"Bombling",
"Bomskit",
"Boo Buddy",
"Boon",
"Bone Putter",
"Bot",
"Boulder",
"Bubble",
"Bulblin",
"Bullbo",
"Business Scrub",
"Buzzblob",
"Camo Goblin",
"Cannon Boat",
"Candle",
"Chaser",
"Chasupa",
"Cheep-Cheep",
"Chilfos",
"Chu",
"Chu Worm",
"ChuChu",
"Cloud Piranha",
"Club Moblin",
"Crab",
"Cranioc",
"Crow",
"Cukeman",
"Cursed Bokoblin",
"Cursed Lizalfos",
"Cursed Moblin",
"Cursed Spume",
"Dacto",
"Daira",
"Dark ChuChu",
"Dark Keese",
"Dark Lizalfos",
"Dark Train",
"Darknut",
"Deadrock",
"Death Armos",
"Deeler",
"Deep Python",
"Deku Baba",
"Deku Like",
"Deku Scrub",
"Desbreko",
"Devalant",
"Dexihand",
"Dexivine",
"Dinolfos",
"Dodongo",
"Doomknocker",
"Dragonfly",
"Eeno",
"Electro Spume",
"Ergtorok",
"Eye Plant",
"Eye Slug",
"Eyeball Monster",
"Eyegore",
"Fin Piranha",
"Fire Baba",
"Fire Keese",
"Fire Toadpoli",
"Floormaster",
"Flying Fish",
"Flying Pot",
"Flying Tile",
"Fokka",
"Fokkeru",
"Force Gem Mimic",
"Freezard",
"Froak",
"Frostare Larva",
"Furnix",
"Garo Robe",
"Gel",
"Geldarm",
"Geldman",
"Gerudo Guard",
"Gerudo Thief",
"Gerune",
"Ghini",
"Ghoul Rat",
"Giant Bee",
"Giant Blade Trap",
"Gibdo",
"Gibo",
"Gigabari",
"Girobokku",
"Glowing Eyeball",
"Gohma",
"Gohma Larva",
"Gold Phantom",
"Golden Octorok",
"Golden Rope",
"Golden Tektite",
"Good Bee",
"Goomba",
"Goponga Flower",
"Goriya",
"Goron Golem",
"Green Bubble",
"Green ChuChu",
"Guardian",
"Guay",
"Guillotine",
"Guma",
"Gyorg",
"Gyorm",
"Hardhat Beetle",
"Heatoise",
"Helmasaur",
"Helmasaurus",
"Helmet ChuChu",
"Hiploop",
"Hokbok",
"Horriblin",
"Hrok",
"Hue",
"Hylian Hornet",
"Hyrule Guard",
"Ice Bubble",
"Ice ChuChu",
"Ice Keese",
"Imp Poe",
"Infinite Hand",
"Iron Knuckle",
"Iron Mask",
"Kargaroc",
"Keaton",
"Keese",
"Keese Swarm",
"Key Master",
"Kodondo",
"King Bubble",
"Ku",
"Kyameron",
"Lakitu",
"Lanmola",
"Leever",
"Like Like",
"Lizalfos",
"Lobarrier",
"Lorule Guard",
"Lynel",
"Mad Bomber",
"Mad Scrub",
"Magma Spume",
"Magnite",
"Mago",
"Magtail",
"Malgyorg",
"Mau",
"Megmat",
"Mask-Mimic",
"Meter Giant",
"Mighty Darknut",
"Mighty Zora Warrior",
"Mini Freezard",
"Mini-Moldorm",
"Miniblin",
"Moa",
"Moblin",
"Moblin Statue",
"Moby",
"Moink",
"Moldola",
"Moldorm",
"Moldworm",
"Morth",
"Moth",
"Mothula",
"Mulldozer",
"Myu",
"Nejiron",
"Nocturn",
"Nuranuru",
"Octive",
"Octoballoon",
"Octomine",
"Octorok",
"Pairodd",
"Paraocto",
"Parasitic Tentacle",
"Patra",
"Peahat",
"Peahat Larva",
"Pengator",
"Pesto",
"Phantom",
"Phantom Eye",
"Phantom Rider",
"Pikit",
"Pincer",
"Piranha Plant",
"Pirogusu",
"Podobos",
"Poe",
"Poison Mite",
"Pokey",
"Pols Voice",
"Popo",
"Puffstool",
"Puppet",
"Pygmy Skulltula",
"Pyrup",
"Quadro Baba",
"Ra",
"Rabbit Fang",
"Rat",
"Raven",
"Real Bombchu",
"Reapling",
"Red Bubble",
"Red ChuChu",
"ReDead",
"Remlit",
"River Zora",
"Rock ChuChu",
"Rollobite",
"Ropa",
"Rope",
"Rupee Like",
"Rupee Wraith",
"Snap Dragon",
"Sandworm",
"Sea Urchin",
"Sentrobe",
"Shabom",
"Shadow Beast",
"Shadow Insect",
"Shadow Kargaroc",
"Shell Blade",
"Shell Spinner",
"Shrouded Stalfos",
"Sir Frosty",
"Sky Tail",
"Skullfish",
"Skulltula",
"Skullwalltula",
"Sluggula",
"Snap Dragon",
"Snapper",
"Snurglar",
"Snurgle",
"Spark",
"Spike",
"Spiked Beetle",
"Spinut",
"Spiny Beetle",
"Squiddy",
"Stag Beetle",
"Stalchild",
"Staldra",
"Stalfos",
"Stalfos Knight",
"Stalfos Warrior",
"Stalkin",
"Stalhound",
"Stalkoblin",
"Star",
"Stinger",
"Swamola",
"Swift Phantom",
"Tailpasaran",
"Takkuri",
"Tank",
"Taurus",
"Technoblin",
"Tektite",
"Terrorpin",
"Three-of-a-Kind",
"Thunder Keese",
"Thwimp",
"Thwomp",
"Tile Worm",
"Tinsuit",
"Toado",
"Torch Phantom",
"Torch Slug",
"Turtle",
"Twilight Assassin",
"Twilit Baba",
"Twilit Bulblin",
"Twilit Keese",
"Twilit Vermin",
"Vengas",
"Venus Flytrap",
"Vire",
"Vulture",
"Wallmaster",
"Wallmaster",
"Warp Phantom",
"Warship",
"Water Spume",
"Water Toadpoli",
"Watcher",
"White Bubble",
"White ChuChu",
"White Wolfos",
"Winder",
"Wizard",
"Wizzrobe",
"Wolfos",
"Wrecker Phantom",
"Yellow ChuChu",
"Yiga Blademaster",
"Yiga Footsoldier",
"Yook",
"Young Gohma",
"Zol",
"Zombie",
"Zora Warrior",
"Little Frox",
"Evermean",
"Aerocuda",
"Gloom Spawn",
"Flame Gleeok", 
"Frost Gleeok",
"Thunder Gleeok",
"King Gleeok",
"Frox",
"phantom ganon",
"Bokoblins",
"Boss Bokoblins",
"Zonai Constructs",
"Horriblins",
"Moblins",
"Octoroks",
"Wizzrobe",
"Yiga Clan",
"Pebblit",
"Flux Construct"]

c = 0
for i in MonsterList:
	MonsterList[c] = i.lower()
	c += 1
