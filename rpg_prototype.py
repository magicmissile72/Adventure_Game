# python RPG
#
import random
from game_map import world, map

# Load the map file
#...this also allows us to change topologies easy, but
# ties this file to us.

LIGHT = "light"

def initialize():
	# initialize the game
	# set any global variables used
	global location
	global debug
	global stuff
	global item_list
	# 0 = no debugging
	# 1 = basic engine and movement functionality
	debug = 0
	# This gives us a random starting location
	# future changes: create an initialization function
	location = "A00"
	#item_list = {
	#				"item_01" : "knife" ,
	#				"item_02" : "key" ,
	#				"item_03" : "gold" ,
	#				"item_04" : "food" ,
	#				"item_05" : "junk" ,
	#				"item_06" : "map"
	#			}
	# Randomly put the six items throughot the maze
	#for key, value in item_list.iteritems():
	#	x = random.randrange(1 , 17)
	#	world[x].update({key : value})
	#
	#stuff = {
	#			"slot 1" : "empty" ,
	#			"slot 2" : "empty" ,
	#			"slot 3" : "empty" ,
	#			"slot 4" : "empty"
	#		}
	#
#
def intro():
	print '''
	Welcome to the trackless waste advernture game...
	
	
	'''
#
def help(what):
	if what == "look":
		print '''\n\t'look; help menu
---------------------------------------------------
look\t\tShows what room you are in
look help\tThis menu
look path\tShow the known paths out of the room
look <object>\tExamine any objects ort items that you can see in the room in more detail
look map\tShows the map, if you have a map
look more\tShow the detailed room description, the known paths, and any objects or special features

'''
		return
	elif what == "path":
		print '''\n\t'go' where?
---------------------------------------------------
go\t\tMove in a desired direction - 10d or 10 possible directions
go help\t\tThis menu...

go north\tor 'n'\tif a valid path exists
go northeast\tor 'nw'\tif a valid path exists
go east\t\tor 'e'\tif a valid path exists
go southeast\tor 'se'\tif a valid path exists
go south\tor 's'\tif a valid path exists
go southwest\tor 'sw'\tif a valid path exists
go west\t\tor 'w'\tif a valid path exists
go northwest\tor 'nw'\tif a valid path exists
go up\t\tor 'u'\tif a valid path exists
go down\t\tor 'd'\tif a valid path exists

'''
		return
	else:
		# general help
		print "\n"
		print "\tThe Help Menu"
		print "============================================================================"
		print "quit\t\tEnd the game"
		print "help\t\tThis menu"
		print "look\t\tLook about and see your surroundings"
		print " - try 'look help'"
		print "go\t\tMove in a desired direction:"
		print " - try 'go help'"
		print "search\t\tTry to finds things in the room"
		print "take\t\tPick up or take an item that you can carry"
		print "drop\t\tPut down or drop an item that you are carrying"
		print "use\t\tUse or activate and item or object"
		print "open\t\tOpen a door or container"
		print "close\t\tClose a door or container"
		print "attack\t\tAttack an enemy"
		print "heal\t\tHeal from damage if you have a medical kit"
		print "inv\t\tShow your Inventory, all the items you are carrying"
		print "\n"
		return
#
#
def command():
	# this starts the infinite loop of the core game engine
	# get input, run command, stir and repeat...
	while True:
		# get the user commands and convert to all lower case
		get_command = raw_input("> ").lower()
		if get_command == "":
			# if the user just hits the enter key, circle back to request input...no big deal
			continue
		commands = get_command.split()
		# commands are 'action' target' so we split on space and then process the commands
		# below gives is the user input, which will now be a list so we can access each word
		# example:
		# ['go', 'west']
		if commands[0] == "quit":
			# quit the game
			print "quitting..."
			break
		elif commands[0] == "go":
			# the 'go' command
			# requires an arugment such as a direction
			# we send that to the direction function for further processing and error checking
			if len(commands) < 2:
				print "Go where?"
			else:
				direction(commands[1])
		elif commands[0] == "help":
			# This command is working...
			# displays the help menu from the help function
			help("none")
		elif commands[0] == "look":
			# pass key word 'more' if present to show the detailed room description
			if len(commands) < 2:
				commands.insert( 1, "none")
				status(commands[1])
			else:
				status(commands[1])
		elif commands[0] == "search":
			if debug == 1 : print "Debug: 'search' was issued"
			if debug == 1 : print "Debug: go to the 'status' function"
			search()
		elif commands[0] == "take":
			# This command is working...
			if debug == 1 : print "Debug: 'take' was issued"
			if debug == 1 : print "Debug: go to the 'status' function"
			take(commands[1])
		elif commands[0] == "drop":
			# This command is working...
			if debug == 1 : print "Debug: 'drop' was issued"
			if debug == 1 : print "Debug: go to the 'status' function"
			drop(commands[1])
		elif commands[0] == "use":
			if debug == 1 : print "Debug: 'use' was issued"
			if debug == 1 : print "Debug: go to the 'status' function"
			use()
		elif commands[0] == "open":
			if debug == 1 : print "Debug: 'open' was issued"
			if debug == 1 : print "Debug: go to the 'status' function"
			open()
		elif commands[0] == "close":
			if debug == 1 : print "Debug: 'close' was issued"
			if debug == 1 : print "Debug: go to the 'status' function"
			status()
		elif commands[0] == "attack":
			if debug == 1 : print "Debug: 'attack' was issued"
			if debug == 1 : print "Debug: go to the 'status' function"
			attack()
		elif commands[0] == "heal":
			if debug == 1 : print "Debug: 'heal' was issued"
			if debug == 1 : print "Debug: go to the 'status' function"
			heal()
		elif commands[0] == "inv":
			# This command is working...
			if debug == 1 : print "Debug: 'inv' for 'inventory' was issued"
			if debug == 1 : print "Debug: go to the 'status' function"
			inventory()
		else:
			# This command is working...
			print "You entered an unknown commmad..."
			print "Please enter a valid command"
			print "Try 'help' to see a list of command options"

#
def direction(move):
	global location
	# below retunrsd the current room 'key' value, example:
	# A00
	#if debug == 1 : print "Debug: current 'location' is: %s" % (location)
	#
	# below gives is the 2nd word from our command 'go direction'
	# move is the value of 'command[1]' and should be one of the ten valid directions
	#if debug == 1 : print "Debug: move = %s" % (move)
	#
	# below gives us the dictionary that is the value of the 'key'
	# example from room 16
	# {'light': 1, 'desc': 'You are in the library. It is filled with many books', 'north': 12, 'name': 'library', 'first': 0}
	#if debug == 1 : print "Debug: world[location] = %s" % (world[location])
	#
	# start direction testing
	if move == "help":
		# > 'go' 'help'
		help("path")
		return
	elif move == "north" or move == "n" :
		if move == "n" : move = "north"
		#if debug == 1 : print "Debug: inside 'if north'"
		#if debug == 1 : print "Debug: %s" % (world[location].has_key("north"))
		#
		if world[location]["north"] == 0 :
			print "You can't go that way"
			return
		elif world[location].has_key("north") == True:
			location = world[location][move]
			print "You go to the north"
			status("none")
			return
		else:
			print "something is wrong with you trying to go north..."
			return
	elif move == "northeast" or move == "ne" :
		if move == "ne" : move = "northeast"
		if world[location]["northeast"] == 0 :
			print "You can't go that way"
			return
		elif world[location].has_key("northeast") == True:
			location = world[location][move]
			print "You go to the northeast"
			status("none")
			return
		else:
			print "something is wrong with you trying to go northeast..."
			return
	elif move == "east" or move == "e" :
		if move == "e" : move = "east"
		if world[location]["east"] == 0 :
			print "You can't go that way"
			return
		elif world[location].has_key("east") == True:
			location = world[location][move]
			print "You go to the east"
			status("none")
			return
		else:
			print "something is wrong with you trying to go east..."
			return
	elif move == "southeast" or move == "se" :
		if move == "se" : move = "southeast"
		if world[location]["southeast"] == 0 :
			print "You can't go that way"
			return
		elif world[location].has_key("southeast") == True:
			location = world[location][move]
			print "You go to the southeast"
			status("none")
			return
		else:
			print "something is wrong with you trying to go southeast..."
			return
	elif move == "south" or move == "s" :
		if move == "s" : move = "south"
		if world[location]["south"] == 0 :
			print "You can't go that way"
			return
		elif world[location].has_key("south") == True:
			location = world[location][move]
			print "You go to the south"
			status("none")
			return
		else:
			print "something is wrong with you trying to go south..."
			return
	elif move == "southwest" or move == "sw" :
		if move == "sw" : move = "southwest"
		if world[location]["southwest"] == 0 :
			print "You can't go that way"
			return
		elif world[location].has_key("southwest") == True:
			location = world[location][move]
			print "You go to the southwest"
			status("none")
			return
		else:
			print "something is wrong with you trying to go southwest..."
			return
	elif move == "west" or move == "w" :
		if move == "w" : move = "west"
		if world[location]["west"] == 0 :
			print "You can't go that way"
			return
		elif world[location].has_key("west") == True:
			location = world[location][move]
			print "You go to the west"
			status("none")
			return
		else:
			print "something is wrong with you trying to go west..."
			return
	elif move == "northwest" or move == "nw" :
		if move == "nw" : move = "northwest"
		if world[location]["northwest"] == 0 :
			print "You can't go that way"
			return
		elif world[location].has_key("northwest") == True:
			location = world[location][move]
			print "You go to the northwest"
			status("none")
			return
		else:
			print "something is wrong with you trying to go northwest..."
			return
	elif move == "up" or move == "u" :
		if move == "u" : move = "up"
		if world[location]["up"] == 0 :
			print "You can't go that way"
			return
		elif world[location].has_key("up") == True:
			location = world[location][move]
			print "You go up"
			status("none")
			return
		else:
			print "something is wrong with you trying to go up..."
			return
	elif move == "down" or move == "d" :
		if move == "d" : move = "down"
		if world[location]["down"] == 0 :
			print "You can't go that way"
			return
		elif world[location].has_key("down") == True:
			location = world[location][move]
			print "You go down"
			status("none")
			return
		else:
			print "something is wrong with you trying to go down..."
			return
	else:
		print "Something went wrong with you entering an unknown direction, try again\n"
		return
#

def status(commands):
	# can we see?
	# add future function to check if lights are on
	#
	if commands == "help":
		help("look")
		return
	elif commands == "stars":
		print "You use your celestial navigation skills and determine that you are located in %s" % (location)
		return
	elif commands == "map":
		#for slot in stuff:
		#	if stuff[slot] == "map":
		#		print map
		#		return
		#print "You need to have the map"
		return
	elif commands == "path":
		exits(1)
		return
	elif commands == "detail":
		exits(2)
		return
	elif commands == "items":
		return
		# add this later...
		#item_list = ["item_01" , "item_02" , "item_03" , "item_04" , "item_05" , "item_06" ]
		count = 0
		for item in item_list:
			if world[location].has_key(item) == True:
				count += 1
				print "You see a %s here." % (world[location][item])
		if count == 0:
			print "There are no items here that you can see"
		return
	elif (commands == "none") or (commands == "more") :
		# Can we see? Is the room dark?
		if world[location][LIGHT] == 0:
			print "It is too dark to see. You have no idea where you are"
			return
		else:
			# Have we been here before? If we have been here before, then just show the room
			print "You are in the %s" % (world[location]["name"])
			if (world[location]["first"] == 0) or (commands == "more") :
				# We have now been here, so change the visit to '1' so we know we have been here
				world[location]["first"] = 1
				# print the room description (long description)
				print "Looking around, you see..."
				print world[location]["desc"]
				# print any special objects we see (things we can "look" at
				print world[location]["special"]
				# print any items that are here and we can see them (searched for?)
				items()
				# print any exits we can see
				exits(2)
				return
			elif world[location]["first"] == 1 :
				return
			else:
				print "looking at what?"
				return
		return
	else:
		print "I'm not sure what you are trying to look at..."
#
#
#
def items():
	print "There are no items visible"
	return
#
def exits(what):
	if what == 1:
		print "looking for exits..."
		if world[location]["north"] != 0:
			print "You can go north"
		if world[location]["northeast"] != 0:
			print "You can go northeast"
		if world[location]["east"] != 0:
			print "You can go east"
		if world[location]["southeast"] != 0:
			print "You can go southeast"
		if world[location]["south"] != 0:
			print "You can go south"
		if world[location]["southwest"] != 0:
			print "You can go southwest"
		if world[location]["west"] != 0:
			print "You can go west"
		if world[location]["northwest"] != 0:
			print "You can go northwest"
		if world[location]["up"] != 0:
			print "You can go up"
		if world[location]["down"] != 0:
			print "You can go down"
		return
	elif what == 2:
		if world[location]["north"] != 0:
			print world[location]["desc_n"]
		if world[location]["northeast"] != 0:
			print world[location]["desc_ne"]
		if world[location]["east"] != 0:
			print world[location]["desc_e"]
		if world[location]["southeast"] != 0:
			print world[location]["desc_se"]
		if world[location]["south"] != 0:
			print world[location]["desc_s"]
		if world[location]["southwest"] != 0:
			print world[location]["desc_sw"]
		if world[location]["west"] != 0:
			print world[location]["desc_w"]
		if world[location]["northwest"] != 0:
			print world[location]["desc_nw"]
		if world[location]["up"] != 0:
			print world[location]["desc_u"]
		if world[location]["down"] != 0:
			print world[location]["desc_d"]
		return
	else:
		print "huh?"
		return
#
def search():
	if (debug == 1) or (debug == 2) : print "Debug: inside 'search' function"
	print "the 'search' command has not yet been implemented"
	return
#
# check for empty inventory slot
def find_slot():
	for slot in stuff:
		if stuff[slot] == "empty":
			return slot
	else:
		return "full"
	#
#
#
def is_item_here(item):
	if debug == 3 : print "Debug: inside 'is_item_here' function"
	#item_list = ["item_01" , "item_02" , "item_03" , "item_04" , "item_05" , "item_06" ]
	if debug == 3 : print "Debug: going through the list of items"
	for key , value in item_list.iteritems():
		if debug == 3 : print "Debug: going through the list of items"
		if debug == 3 : print "Debug: key = %s | value = %s" % (key , value)
		if debug == 3 : print "Debug: item = %s" % (item)
		if debug == 3 : print "Debug: check if the item (%s) is in this location" % (item)
		if debug == 3 : print "Debug: location = %s" % (location)
		if value == item:
			if debug == 3 : print "Debug: location/key is True or False:"
			#if debug == 3 : print "Debug: location/key = %s" % (world[location](key))
			if world[location].has_key(key) == True:
				if debug == 3 : print "Debug: item is: %s" % (key)
				return True
	return False
#
def take(item):
	if debug == 3 : print "Debug: inside 'take' function"
	if debug == 3 : print "Debug the 'take/drop/inventory' process"
	# check if the item is even here...
	if debug == 3 : print "Debug: is the 'item' in this room?"
	if debug == 3 : print "Debug: 'item' = %s" % (item)
	test = is_item_here(item)
	if debug == 3 : print "Debug: expecting a 'True' or 'False'"
	if debug == 3 : print "Debug: 'True' means the item is in this room"
	if debug == 3 : print "Debug: 'False' means the item is NOT in this room"
	if debug == 3 : print "Debug: test = %s" % (test)
	if test == True:
		if debug == 3 : print "Debug: True...Pass"
		pass
		# the item exists in this room
	elif test == False:
		if debug == 3 : print "Debug: False"
		print "The %s has to be in the room for you to take it" % (item)
		return
	else:
		if debug == 3 : print "Debug: else"
		print "something is not right here"
		return
	if debug == 3 : print "Debug: test = %s" % (item)
	if debug == 3 : print "Debug: ..."
	if debug == 3 : print "Debug: get the slot to put the item in"
	slot = find_slot()
	if debug == 3 : print "Debug: slot = %s" % (slot)
	#
	if slot == "full":
		print "there are no empty slots, you need to drop something"
		return
	elif item == "knife" :
		stuff.update({slot : "knife"})
		print "You take the %s" % (item)
		del world[location]["item_01"]
	elif item == "key" :
		stuff.update({slot : "key"})
		print "You take the %s" % (item)
		del world[location]["item_02"]
	elif item == "gold" :
		stuff.update({slot : "gold"})
		print "You take the %s" % (item)
		del world[location]["item_03"]
	elif item == "food" :
		stuff.update({slot : "food"})
		print "You take the %s" % (item)
		del world[location]["item_04"]
	elif item == "junk" :
		stuff.update({slot : "junk"})
		print "You take the %s" % (item)
		del world[location]["item_05"]
	elif item == "map" :
		stuff.update({slot : "map"})
		print "You take the %s" % (item)
		del world[location]["item_06"]
	else:
		print "There is nothing like that to take"
		return
#
def find_item_slot(item):
	for slot in stuff:
		if stuff[slot] == item :
			return slot
	else:
		return "missing"
	#
#
def drop(item):
	if debug == 3 : print "Debug: inside 'drop' function"
	if debug == 3 : print "Debug the 'take/drop/inventory' process"
	#
	slot = find_item_slot(item)
	if slot == "missing":
		print "You don't have the %s to drop" % (item)
		return
	#
	if item == "knife" :
		stuff.update({slot : "empty"})
		print "You drop the %s" % (item)
		world[location].update({"item_01" : "knife"})
	elif item == "key" :
		stuff.update({slot : "empty"})
		print "You drop the %s" % (item)
		world[location].update({"item_02" : "key"})
	elif item == "gold" :
		stuff.update({slot : "empty"})
		print "You drop the %s" % (item)
		world[location].update({"item_03" : "gold"})
	elif item == "food" :
		stuff.update({slot : "empty"})
		print "You drop the %s" % (item)
		world[location].update({"item_04" : "food"})
	elif item == "junk" :
		stuff.update({slot : "empty"})
		print "You drop the %s" % (item)
		world[location].update({"item_05" : "junk"})
	elif item == "map" :
		stuff.update({slot : "empty"})
		print "You drop the %s" % (item)
		world[location].update({"item_06" : "map"})
	else:
		print "You don't have anyting like that to drop"
		return
	look_items()
#
def use():
	if (debug == 1) or (debug == 2) : print "Debug: in side 'use' function"
	print "the 'use' command has not yet been implemented"
	return
#
def open():
	if (debug == 1) or (debug == 2) : print "Debug: in side 'open' function"
	print "the 'open' command has not yet been implemented"
	return
#
def close():
	if (debug == 1) or (debug == 2) : print "Debug: in side 'close' function"
	print "the 'close' command has not yet been implemented"
	return
#
def attack():
	if (debug == 1) or (debug == 2) : print "Debug: in side 'attack' function"
	print "the 'attack' command has not yet been implemented"
	return
#
def heal():
	if (debug == 1) or (debug == 2) : print "Debug: in side 'heal' function"
	print "the 'heal' command has not yet been implemented"
	return
#
def inventory():
	if debug == 3 : print "Debug: inside 'inventory' function"
	if debug == 3 : print "Debug the 'take/drop/inventory' process"
	print "You can carry up to four items total. You have:"
	print "Slot 1: %s" % (stuff["slot 1"])
	print "Slot 2: %s" % (stuff["slot 2"])
	print "Slot 3: %s" % (stuff["slot 3"])
	print "Slot 4: %s" % (stuff["slot 4"])
	print
	return
#






# MAIN
# ==============================================================================
#
#
# get our starting values
initialize()
intro()
command()


# EOF