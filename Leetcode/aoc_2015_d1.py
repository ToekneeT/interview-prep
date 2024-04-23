import unittest

# ----- Part 1 -----
# Simple problem.
# Take in a string with parenthesis.
# Have a count variable that represents which floor we're on.
# If it's an open paren, we go up a floor, if it's a closed paren, 
# we go down a floor.

# First step it to take an input.
# Since it's one long string, no newlines
# we can keep it as a string and then just 
# parse through the string with a loop.

with open("aoc_d1_input.txt") as file:
	instructions = file.read()

def which_floor(instruc: str) -> int:
	# Floor keeps track which floor we're on.
	floor = 0
	for c in instruc:
		# Up a floor if it's an open.
		if c == "(":
			floor += 1
		# Down a floor if it's closed.
		else:
			floor -= 1
	return floor

# ----- Part 2 -----
# Find the first position that makes Santa go into the basement.
# This means that at some point in the input, the floor counter is less than zero.
# We just want to find the first time this happens.
# e.x. ) -> means he enters the basement at position 1.
# ()()) -> Means he enters the basement as position 5.

# To modify the first part, we're gonna use a for range loop instead.
# This allows us to get the index of the current position.
def first_basement_occur(instruc: str) -> int:
	floor = 0
	for i in range(len(instruc)):
		if instruc[i] == "(":
			floor += 1
		else:
			floor -= 1
		# The basement is anything under 0, which in this case
		# is the first occurrence it happens, so once hitting -1,
		# we return the index.
		if floor == -1:
			return i + 1


# The first test doesn't matter in these unit tests as I wouldn't
# know the answer until I solved it.
class Test(unittest.TestCase):
	def test_part_one(self):
		#self.assertEqual(which_floor(instructions), 138)
		self.assertEqual(which_floor("()"), 0)
		self.assertEqual(which_floor("("), 1)
		self.assertEqual(which_floor(")"), -1)
		self.assertEqual(which_floor("(()(()("), 3)
		self.assertEqual(which_floor(")())())"), -3)

	def test_part_two(self):
		#self.assertEqual(first_basement_occur(instructions), 1771)
		# The following test made me realize that it doesn't work with
		# this edge case, it wouldn't have worked with my original code.
		# which is the if floor == -1 line at the start of the function.
		# That makes sense since it would check at the beginning of the 
		# next loop, but we wanted to test the condition after we move floors.
		self.assertEqual(first_basement_occur(")"), 1)
		self.assertEqual(first_basement_occur("()())"), 5)
		self.assertEqual(first_basement_occur("())"), 3)

if __name__ == "__main__":
	unittest.main()