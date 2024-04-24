import unittest
'''
 ----- Part 1 -----
Given a single line input containing only <^v>,
figure out how many unique locations have been visited.
Meaning how many locations that haven't been visited yet.
The starting position always counts as 1.
So if the input only contained ">", then the unique locations visited
is equal to 2. Starting position, one to the right.

My thought is to have two count variables acting as a vector.
The vector being a tuple, so position (0, 0) is the start.
One value is the west and east positions, the other is the 
north and south positions.
Going North is positive, going South is negative.
Going East is positive, going West is negative.
Then place the vector in a set so that it doesn't contain any
duplicates. Return the length of the set.

Can make a key dictionary to determine the character it reads
and which number to add to it.
'''


with open("aoc_2015_d3_input.txt") as file:
	directions = file.read()


# Time Complexity: O(n) since it's just going through the length of the string once.
def unique_locations(direc: str) -> int:
	# The character values and what they'll represent.
	north_south_key = {
	"v": -1,
	"^": 1,
	}
	west_east_key = {
	">": 1,
	"<": -1,
	}

	# starting position, (0, 0) is already in the set
	# because the starting location counts as one unique house.
	unique_houses = {(0, 0)}
	# x = west and east, y = north and west.
	# as in x axis and y axis in a 3D plane.
	x, y = 0, 0

	for c in direc:
		# c is the chararcter direction, such as <^v>, which is the 
		# key in the dictionary.
		# By passing it to the dictionary, we'll get the value back
		# which in this case is either +1 or -1, representing either
		# going north, south, east, or west.
		if c in north_south_key:
			y += north_south_key[c]
		else:
			x += west_east_key[c]
		# Add the vector to a set, sets only have unique values, no
		# duplicates are allowed. So passing one that already exists won't
		# change the length of the set, thereby only having unique locations.
		unique_houses.add((x, y))

	return len(unique_houses)

'''
 ----- Part 2 -----
Same concept, except there's a second "thing" delivering presents.
Take turns on instructions. Meaning, >< would be 3 unique locations
instead of 2 from the previous. This is because person one goes right,
then person two goes left. So it should look like this:
P1, P2, where x = starting house.
x -> x P1 -> P2 x P1

A way to solve this is since it's already iterating through the string,
instead of getting the value itself, we can use an index instead.
We can have one person move when the index is even, the other on odd.
To achieve this, we can use modulous of 2.
We can then have two vectors, one for each person.
'''


# Time Complexity: O(n) since it's just going through the length of the string once.
def take_turns(direc: str) -> int:
	north_south_key = {
	"v": -1,
	"^": 1,
	}
	west_east_key = {
	">": 1,
	"<": -1,
	}

	unique_houses = {(0, 0)}
	x1, x2, y1, y2 = 0, 0, 0, 0

	for i in range(len(direc)):
		# One person moves on even indices, the other on odd.
		if direc[i] in north_south_key:
			if i % 2 == 0:
				y1 += north_south_key[direc[i]]
			else:
				y2 += north_south_key[direc[i]]
		else:
			if i % 2 == 0:
				x1 += west_east_key[direc[i]]
			else:
				x2 += west_east_key[direc[i]]
		# Instead of doing another conditional to check
		# if the index is even or odd to add that specific
		# vector to the set, we can just add them both anyway
		# since the previous value should already be in the set.
		unique_houses.add((x1, y1))
		unique_houses.add((x2, y2))

	return len(unique_houses)


class Test(unittest.TestCase):
	def test_unique_locations(self):
		self.assertEqual(unique_locations(">"), 2)
		self.assertEqual(unique_locations(""), 1)
		self.assertEqual(unique_locations("^>v<"), 4)
		self.assertEqual(unique_locations("^v^v^v^v^v"), 2)

	def test_take_turns(self):
		self.assertEqual(take_turns("^v"), 3)
		self.assertEqual(take_turns("><"), 3)
		self.assertEqual(take_turns("^>v<"), 3)
		self.assertEqual(take_turns("^v^v^v^v^v"), 11)
		self.assertEqual(take_turns(""), 1)

if __name__ == "__main__":
	unittest.main()