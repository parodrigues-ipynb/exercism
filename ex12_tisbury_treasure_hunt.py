# Personal notes
"""
This learning exercise helped evolve your knowledge of Tuples.

A tuple is an immutable collection of items in sequence. Therefore, tuples
doesn't support mutable sequence operations.

Like most collections, tuples can hold any (or multiple) data types.

Tuples can be formed in multiple ways, using either:
>>> no_elements = tuple()
>>> no_elements
()
>>> no_elements = ()
>>> no_elements
()

>>> multiple_elements_string = tuple('Bernadete')
>>> multiple_elements_string
('B', 'e', 'r', 'n', 'a', 'd', 'e', 't', 'e')

Tuples can be concatenated using the + operator, which unpacks each
tuple creating a new, combined tuple.
>>> new_via_concatenate = ('George', 5) + ('cat', 'Tabby')
('George', 5, 'cat', 'Tabby')

>>> first_group = ('cat', 'dog')
>>> multiplied_group = first_group * 3
('cat', 'dog', 'cat', 'dog', 'cat', 'dog')

Elements within a tuple can be accessed via backet notation.
>>> student_info = ('Alyssa', 'grade 3', 'female', 8)
>>> student_name = student_info[0]
'Alyssa'

You can use the following loops:
for item in <tuple>
for index, item in enumerate(<tuple>)

And you can also copy tuples using slice notation:
<tuple>[start:stop:step]

You can use the in operator to check for membership.
>>> multiple_elements_list = tuple(['Ragnarök', 'Pauper'])
>>> pauper in multiple_elements_list
True
"""

# Instructions
"""
Azara and Rui are teammates competing in a pirate-themed treasure hunt.

One has a list of treasures with map coordinates, the other a list of location
names with map coordinates. They've also been given blank maps with a starting
place marked YOU ARE HERE.

AZARA'S LIST-------------------------------
Treasure 	                    Coordinates
Amethyst Octopus 	            1F
Angry Monkey Figurine 	        5B
Antique Glass Fishnet Float 	3D
Brass Spyglass 	                4B
Carved Wooden Elephant 	        8C
Crystal Crab 	                6A
Glass Starfish 	                6D
Model Ship in Large Bottle 	    8A
Pirate Flag 	                7F
Robot Parrot 	                1C
Scrimshawed Whale Tooth 	    2A
Silver Seahorse 	            4E
Vintage Pirate Hat 	            7E
-------------------------------------------

RUI'S LIST------------------------------------------------------
Location Name 	                        Coordinates     Quadrant
Seaside Cottages 	                    ("1", "C") 	    Blue
Aqua Lagoon (Island of Mystery) 	    ("1", "F") 	    Yellow
Deserted Docks 	                        ("2", "A") 	    Blue
Spiky Rocks 	                        ("3", "D") 	    Yellow
Abandoned Lighthouse 	                ("4", "B") 	    Blue
Hidden Spring (Island of Mystery) 	    ("4", "E") 	    Yellow
Stormy Breakwater 	                    ("5", "B") 	    Purple
Old Schooner 	                        ("6", "A") 	    Purple
Tangled Seaweed Patch 	                ("6", "D") 	    Orange
Quiet Inlet (Island of Mystery) 	    ("7", "E") 	    Orange
Windswept Hilltop (Island of Mystery) 	("7", "F") 	    Orange
Harbor Managers Office 	                ("8", "A") 	    Purple
Foggy Seacave 	                        ("8", "C")      Purple
----------------------------------------------------------------

But things are a bit disorganized: Azara's coordinates appear to be
formatted and sorted differently from Rui's, and they have to keep
looking from one list to the other to figure out which treasures
go with which locations.

Being budding pythonistas, they have come to you for help in writing
a small program to better organize their hunt information
"""

# 1. Extract coordinates
"""
Implement the get_coordinate() function that takes a (treasure, coordinate)
pair from Azara's list and returns only the extracted map coordinate.
"""


def get_coordinate(record):
    return record[1]


# 2. Format coordinates
"""
Implement the convert_coordinate() function that takes a coordinate in the format
"2A" and returns a tuple in the format ("2", "A").
"""


def convert_coordinate(coordinate):
    return tuple(coordinate)


# 3. Match coordinates
"""
Implement the compare_records() function that takes a (treasure, coordinate) pair
and a (location, coordinate, quadrant) record and compares coordinates from each.

Return True if the coordinates "match" and False if they do not.

Re-format coordinates as needed for accurate comparison.

--------- AZARA'S FORMAT ---------
Amethyst Octopus 	            1F

----------------- RUI'S FORMAT ---------------------
Seaside Cottages 	            ("1", "C") 	    Blue
"""


def compare_records(azara_record, rui_record):
    return convert_coordinate(get_coordinate(azara_record)) == get_coordinate(rui_record)


# 4. Combined matched records
"""
Implement the create_record() function that

takes a
(treasure, coordinate)
pair from Azara's list

and a
(location, coordinate, quadrant)
record from Rui's list

and returns
(treasure, coordinate, location, coordinate, quadrant)
if the coordinates match.

If the coordinates do not match, return the string "not a match".

Re-format the coordinates as needed for accurate comparison.
"""


def create_record(azara_record, rui_record):
    return azara_record + rui_record if compare_records(azara_record, rui_record) else "not a match"


# 5. Clean up and make a report of all records
"""
Clean up the combined records from Azara and Rui so that there's only one
set of coordinates per record.

Make a report so they can see one list of everything they need to put on
their maps.

Implement the clean_up() function that takes a tuple of tuples (everything
from both lists), looping throught the outer tuple, dropping the unwanted
coordinates from each inner tuple and adding each to a "report".

Format and return the "report" so that there is one cleaned record on each
line.

>>> combined_record_group = ( (
        ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'),                   # record 0
        ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'),  # record 1
        ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')                            # record 2
) )

>>> record = combined_record_group[0]   # record
('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')

>>> record[:1]
('Brass Spyglass',)

>>> record[2:]
('Abandoned Lighthouse', ('4', 'B'), 'Blue')

>>> cleaned_up = record[:1] + record[2:]
('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')
"""


def clean_up(combined_record_group):
    report = ""
    for record in combined_record_group:
        cleaned_up = record[:1] + record[2:]
        report += f"{cleaned_up}\n"
    return report
