import unittest
'''
 ----- Part 1 -----
It's an interesting problem, I personally have a hard time visualizing coordinate grids
like this problem. Given a coordinate grid, 0,0 being top left, 999,0 being top right,
0,999 being bottom left, and 999,999 being bottom right.
Given instructions, perform actions. e.x:
turn off xxx,yyy through xxx,yyy
turn on 0,0 through 999,999 turns on every single light.
toggle 0,0 through 999,0 toggles the first line of 1000 lights, meaning if they're off, they get switched on, off if
they were already on.
turn off, self explantatory.
Return value is how many lights remain on.

All lights are off by default.
Make a count variable that tracks how many lights are on. Add one if turning on, subtract one when turning off.
Do this while taking in the instructions so that it won't need to parse the list after all the instructions to count
the amount of lights on.
The grid itself can probably be a 2D list, 1000 rows, 1000 columns. Each with the value of True or False, dictating
if the light is on or off, true being on, false being off.
Can do this by creating an list of 1000 false values, then multiplying that list by 1000.

----- Started coding after this point -----
There are three types of instructions, but two types use two words for the actionable.
So, we can split the instruction, depending on the length of the instruction, we know it'll be toggle,
or turning on / off.
We can then use hardcoded index values.
If the length is 5 for the instructions, then we look at the second index to see if it's turning on or off the lights.
We can then look at 3 and 5 for the range we're going to look at.
Same idea with toggle, if the length of the instructions is 4, we can look at just 2 and 4 for the range.

Thinking about it some more, I thought maybe I could do with with just math instead of a grid, but knowing that
there's a toggle, I don't think that's the right move anymore.

Probably just use a nested for loop, one going through rows and the other going through columns.
'''

with open("aoc_2015_d6_input.txt") as file:
	instructions = [line.rstrip("\n") for line in file]

def part_one(instructions: list) -> int:
	lights_on = 0
	grid = [[False] * 1000 for i in range(1000)]
	for instruc in instructions:
		instruc = instruc.split()
		row1, col1, row2, col2 = 0,0,0,0
		# Nabs the range which we'll be going through the grid.
		# we do +1 on the end as it's exclusive, and we want it to be inclusive.
		# We'll then split the range by a comma since it's comma separated.
		if len(instruc) == 5 and instruc[1] == "off":
			action = "off"
			row1 = int(instruc[2].split(",")[0])
			col1 = int(instruc[2].split(",")[1])
			row2 = int(instruc[4].split(",")[0])
			col2 = int(instruc[4].split(",")[1])
		elif len(instruc) == 5 and instruc[1] == "on":
			action = "on"
			row1 = int(instruc[2].split(",")[0])
			col1 = int(instruc[2].split(",")[1])
			row2 = int(instruc[4].split(",")[0])
			col2 = int(instruc[4].split(",")[1])
		else:
			action = "toggle"
			row1 = int(instruc[1].split(",")[0])
			col1 = int(instruc[1].split(",")[1])
			row2 = int(instruc[3].split(",")[0])
			col2 = int(instruc[3].split(",")[1])

		# Only change the lights on or off if the light is the opposite of what's happening.
		# Meaning if we're turning a light on, and the light is off, we'll add. But if the light is already on,
		# we don't need to add anything.
		for row in range(row1, row2 + 1):
			for col in range(col1, col2 + 1):
				if action == "on":
					if not grid[row][col]:
						lights_on += 1
					grid[row][col] = True
				elif action == "off":
					if grid[row][col]:
						lights_on -= 1
					grid[row][col] = False
				else:
					if grid[row][col]:
						grid[row][col] = False
						lights_on -= 1
					else:
						grid[row][col] = True
						lights_on += 1

	return lights_on

'''
 ---- Part 2 -----
The problem changes enough that it warrants a decent change in program.
Instead of booleans for the values, we'll have numbers that increase or decrease based on the input.
turn on increases the light by 1, turn off decrease by 1, toggle increases by 2.
Brightness can't be under 0.
Return the total brightness.
It's relatively the same, we'll just need to track the brightness.
At first, I considered the fact that we can just use math, on add 1, off sub 1, tog add 2.
But then I realized that wont be possible since the minimum brightness is zero, can't go under.
'''
def part_two(instructions: list) -> int:
	brightness = 0
	grid = [[0] * 1000 for i in range(1000)]
	for instruc in instructions:
		instruc = instruc.split()
		row1, col1, row2, col2 = 0,0,0,0
		if len(instruc) == 5 and instruc[1] == "off":
			action = "off"
			row1 = int(instruc[2].split(",")[0])
			col1 = int(instruc[2].split(",")[1])
			row2 = int(instruc[4].split(",")[0])
			col2 = int(instruc[4].split(",")[1])
		elif len(instruc) == 5 and instruc[1] == "on":
			action = "on"
			row1 = int(instruc[2].split(",")[0])
			col1 = int(instruc[2].split(",")[1])
			row2 = int(instruc[4].split(",")[0])
			col2 = int(instruc[4].split(",")[1])
		else:
			action = "toggle"
			row1 = int(instruc[1].split(",")[0])
			col1 = int(instruc[1].split(",")[1])
			row2 = int(instruc[3].split(",")[0])
			col2 = int(instruc[3].split(",")[1])


		for row in range(row1, row2 + 1):
			for col in range(col1, col2 + 1):
				if action == "on":
					brightness += 1
					grid[row][col] += 1
				elif action == "off" and grid[row][col] != 0:
					brightness -= 1
					grid[row][col] -= 1
				elif action == "toggle":
					brightness += 2
					grid[row][col] += 2

	return brightness


class Test(unittest.TestCase):
	def test_part_one(self):
		self.assertEqual(part_one(["turn on 0,0 through 2,2"]), 9)
		self.assertEqual(part_one(["turn on 0,0 through 0,0"]), 1)
		self.assertEqual(part_one(["turn on 0,0 through 1,0"]), 2)
		self.assertEqual(part_one(["turn on 0,0 through 1,1"]), 4)
		self.assertEqual(part_one(["turn on 499,499 through 500,500"]), 4)
		self.assertEqual(part_one(["turn on 499,499 through 500,500", "turn off 499,499 through 500,500"]), 0)
		self.assertEqual(part_one(["toggle 499,499 through 500,500"]), 4)

	def test_part_two(self):
		self.assertEqual(part_two(["turn on 0,0 through 0,0"]), 1)
		self.assertEqual(part_two(["toggle 0,0 through 999,999"]), 2000000)
		self.assertEqual(part_two(["turn off 0,0 through 0,0"]), 0)
		self.assertEqual(part_two(["turn on 0,0 through 0,1", "turn off 0,0 through 0,0"]), 1)

if __name__ == "__main__":
	unittest.main()