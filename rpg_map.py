# python RPG
# +----------+----------+----------+----------+
# |     1    |     2    |     3    |     4    |
# |  kitchen    dining     lounge  |  closet  |
# |          |    room  |          |          |
# +----  ----+----  ----+----  ----+----  ----+
# |     5    |     6    |     7    |     8    |
# |  pantry  |   grand      bath      bedroom |
# |          |    hall  |   room   |          |
# +----------+----  ----+----------+----  ----+
# |     9    |    10    |    11    |    12    |
# |   study      grand     waiting     east   |
# |          |    hall  |   room   |   hall   |
# +----  ----+----  ----+----------+----  ----+
# |    13    |    14    |    15    |    16    |
# |  sitting   entrance    closet  |  library |
# |   room   |          |          |          |
# +----------+----------+----------+----------+
#
#     N
#     |
#   W-+-E
#     |
#     S
#
map = '''

+----------+----------+----------+----------+
|          |          |          |          |
|  kitchen    dining     lounge  |  closet  |
|          |    room  |          |          |
+---+  +---+---+  +---+---+  +---+---+  +---+
|          |          |          |          |
|  pantry  |   grand      bath      bedroom |
|          |    hall  |   room   |          |
+----------+-+      +-+----------+---+  +---+
|          |          |          |          |
|   study      grand     waiting     east   |
|          |    hall  |   room   |   hall   |
+---+  +---+---+  +---+----------+---+  +---+
|          |          |          |          |
|  sitting   entrance    closet  |  library |
|   room   |          |          |          |
+----------+----------+----------+----------+

\t\tN
\t\t^
\t\t|

'''
# The MAP
rooms = {
		1 : {
				"name"       : "kitchen" ,
				"east"       :  2 ,
				"south"      :  5 ,
				"desc_east"  : "You can see a room toward the east." ,
				"desc_south" : "You can see a room toward the south." ,
				"light"      :  1 ,
				"first"      :  0 ,
				"item_01"    : "knife" ,
				"desc"       : "\nThe kitchen is a large room with many cabinets and a lot of counter\nspace. There is even a small island in the middle. There is a stove and\nan ice box along with a bunch of pots, pans, and cooking utensils\nstrewn about.\n"
			} ,
		
		2 : {
				"name"       : "dining room" ,
				"east"       :  3 ,
				"south"      :  6 ,
				"west"       :  1 ,
				"desc_east"  : "You can see a room toward the east" ,
				"desc_south" : "You can see a room toward the south" ,
				"desc_west"  : "You can see a room toward the west" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nIn this formal dining room is a large table here with seating for ten.\nThe places are set with plates, silverware, napkins, and glassware.\nThere is a large chandeler hanging from the ceiling.\n"
			} ,
			  
		3 : {
				"name"       : "lounge" ,
				"south"      :  7 ,
				"west"       :  2 ,
				"desc_south" : "You can see a room toward the south" ,
				"desc_west"  : "You can see a room toward the west" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nThe lounge area is a comfortable room and a nice place in which to\nrelax. There are several comfy looking chairs and a coffee table with\n some stale cookies.\n"
			} ,

		4 : {
				"name"       : "closet" ,
				"south"      :  8 ,
				"desc_south" : "You can see a room toward the south" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nThis is obviously a Master bedroom closet. There are a lot of coats\nand other clothing hung in here. There are several racks for shoes and\nother accessories like belts and watches. Several cabinets with\ndrawers hold additonal storage. There is a small bench seat for changing.\n"
			} ,

		5 : {
				"name"       : "pantry" ,
				"north"      :  1 ,
				"desc_north" : "You can see a room toward the north" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nThe food pantry is full of shelves and crates on the floor. Several\nsacks of food are also on the floor containing grains, rice, and\npotatos. The shelves are full of canned goods and some aging meats are\nhanging from the ceiling.\n"
			} ,
		
		6 : {
				"name"       : "north grand hall" ,
				"north"      :  2 ,
				"east"       :  7 ,
				"south"      : 10 ,
				"desc_north" : "You can see a room toward the north" ,
				"desc_east"  : "You can see a room toward the east" ,
				"desc_south" : "You can see a room toward the south" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nThe Grand hall way runs north and south along the center of the\nmansion. You are in the north end of the hall which extends to the south.\nThere are fine tapestries and paintings on the wall as well as a few\nbusts of famous people.\n"
			} ,
			  
		7 : {
				"name"       : "bathroom" ,
				"north"      :  3 ,
				"east"       :  8 ,
				"west"       :  6 ,
				"desc_north" : "You can see a room toward the north" ,
				"desc_east"  : "You can see a room toward the east" ,
				"desc_west"  : "You can see a room toward the west" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nThis is the one and only bathroom in the mansion. It is a large and\nwell connected room with all the ammenities one would expect. Towels\nare folded on a rack. There is a claw foot tub and marble and glass\nshower, a private stall housing a toilet, several sinks. Flowers and\npaintings adorn the room.\n"
			} ,

		8 : {
				"name"       : "bedroom" ,
				"north"      :  4 ,
				"south"      : 12 ,
				"west"       :  7 ,
				"desc_north" : "You can see a room toward the north" ,
				"desc_south" : "You can see a room toward the south" ,
				"desc_west"  : "You can see a room toward the west" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nThis is a beasutful and conmfortable bedroom with a king-sized four\npost bed against the wall. Beautiful tapestries adorn the walls.\nThere is a close dressor and night stands next to the bed. There is also a\ndressing table and chair.\n"
			} ,

		9 : {
				"name"       : "study" ,
				"east"       : 10 ,
				"south"      : 13 ,
				"desc_east"  : "You can see a room toward the east" ,
				"desc_south" : "You can see a room toward the south" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nThe study has a large desk and leather backed chair in the center. A \nlamp stands guard next to the desk. There are several chairs\nand book shelves along the walls. There is a fireplace here and large\npainting hangs above the hearth.\n"
			} ,
		
		10 : {
				"name"       : "south grand hall" ,
				"north"      :  6 ,
				"east"       : 11 ,
				"south"      : 14 ,
				"west"       :  9 ,
				"desc_north" : "You can see a room toward the north" ,
				"desc_east"  : "You can see a room toward the east" ,
				"desc_south" : "You can see a room toward the south" ,
				"desc_west"  : "You can see a room toward the west" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nThe Grand hall way runs north and south along the center of the\nmansion. You are in the south end of the hall which extends to the north.\nThere are fine tapestries and paintings on the wall as well as a few\nbusts of famous people.\n"
			} ,
			  
		11 : {
				"name"       : "waiting room" ,
				"east"       : 12 ,
				"west"       : 10 ,
				"desc_east"  : "You can see a room toward the east" ,
				"desc_west"  : "You can see a room toward the west" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nThe room is actually an east to west hallway, but it has plush benches\nagaisnt the north and south walls and is intended to host guests\nwhile waiting for the master.\n"
			} ,

		12 : {
				"name"       : "east hall" ,
				"north"      :  8 ,
				"south"      : 16 ,
				"west"       : 11 ,
				"desc_north" : "You can see a room toward the north" ,
				"desc_south" : "You can see a room toward the south" ,
				"desc_west"  : "You can see a room toward the west" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nThe east hall which runs north and south along the east side of the\nmansion. it connects to the west to the rest of the mansion. There is\nnothing special about this room.\n"
			} ,
			  
		13 : {
				"name"       : "sitting room" ,
				"north"      :  9 ,
				"east"       : 14 ,
				"desc_north" : "You can see a room toward the north" ,
				"desc_east"  : "You can see a room toward the east" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nThe room looks like it was originally planned to be a bedroom, but\nwas changed to more formal function. It now houses a couch and several\ncomfy chairs. It is probably closer to a living room in appearance.\n"
			} ,
		
		14 : {
				"name"       : "entrance" ,
				"north"      : 10 ,
				"east"       : 15 ,
				"west"       : 13 ,
				"desc_north" : "You can see a room toward the north" ,
				"desc_east"  : "You can see a room toward the east" ,
				"desc_west"  : "You can see a room toward the west" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nThis is main entrance foyer to the mansion. It is a grand entance and\nyou can see to the north, it continues on into the grand hallway of\nthe mansion.\n"
			} ,
			  
		15 : {
				"name"       : "closet" ,
				"west"       : 14 ,
				"desc_west"  : "You can see a room toward the west" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nThis closet is for the guests coats, clothing, and shoes. There is a\nlot of room here along with a bench and chairs for guest to change\ntheir shoes or coats comfortably.\n"
			} ,

		16 : {
				"name"       : "library" ,
				"north"      : 12 ,
				"desc_north" : "You can see a room toward the north" ,
				"light"      :  1 ,
				"first"      :  0 ,
				"desc"       : "\nThe library is a rather large room. It is filled with many, many\nbooks that fill the bookshelves that encircle the room and walls. There\nare a number of old and odd lookling scientific instruments here as\nwell and a number of magazines and old newspapers.\n"
			} ,
			  
		}
#