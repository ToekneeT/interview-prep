import unittest
import re
from collections import defaultdict

# ([a-z] AND [a-z]|[a-z] OR [a-z]|[a-z]+|NOT [a-z]|NOT \d+|\d+) (AND|OR|->|LSHIFT|RSHIFT) ([a-z]+)

'''
 ----- Part 1 -----
I'm starting this late, but the first time I read the problem, I was tired and didn't understand what
was going on, so I decided that I'd do it another day. I had to first understand what bitwise was, I had
no clue how the numbers were being assigned to the "wires." Upon further research, it's done on a bit
level. But, luckily, most languages have bitwise operations already done. So for example:
123 AND 456 gives 72. In Python, it'd look like 123 & 456.
There are other expressions too, << LSHIFT, >> RSHIFT, | OR, & AND, ^ XOR (not in the problem), ~ NOT.

Now that I understood the problem, it seems quite simple of a day. But, the issue now is that I would like to use
Regex on this problem, and I have no prior experience using Regex. I have been working on Regex for a bit now, and
I have made some progress, but not significant.

After getting some advice, it seems that hybrid parsing is a good idea, where it's a mix of both Python and Regex.
Seeing that the input is always ending in -> [a-z], I will probably just chop off the last two items, leaving the 
starting portion, to which I can probably Regex that out.

After getting the Regex part done, I think having a dictionary with the keys being the wire and the value
being the value of the wire would be the next step. Using a default dict in case the value isn't already present.

So it seems that the order of the instructions don't matter. So the value of a given wire could be given later down the
line. So what I'm gonna want to do is probably put each wire into a dictionary as a key and the value being the value of
the wire.
'''

with open('aoc_2015_d7_input.txt') as file:
	instructions = [l.strip() for l in file]


# Performs the bitwise function of two numbers. The action passed is a string that will correspond to which
# function will be done. Does not include the NOT as that only requires one number whereas this is passed two.
def perform_bitwise(wire: int, action: str, wire_two: int) -> int:
	# number = r'(\d+)'
	# match_number = re.search(number, wire_two)
	# if match_number:
	# 	wire_two = int(wire_two)
	if action == 'AND':
		return wire & wire_two
	elif action == 'OR':
		return wire | wire_two
	elif action == 'RSHIFT':
		return wire >> wire_two
	elif action == 'LSHIFT':
		return wire << wire_two


# Given a list of instructions, output what the signal is for wire a
def part_one(instructions: list) -> int:
	# Expressions that look like: lf and lq -> ls
	pattern_one = r'([a-z]+|\d+) (AND|OR|RSHIFT|LSHIFT) ([a-z]+|\d+) -> ([a-z]+)'
	# Expressions that look like: NOT kt -> ku
	pattern_two = r'^NOT ([a-z]+) -> ([a-z]+)'
	# Expressions that look like: x -> y
	pattern_three = r'^([a-z]+) -> ([a-z]+)'
	# Expressions that look like: [0-9] -> y
	# Want this in order to put into the dictionary value.
	pattern_number = r'(^\d+) -> ([a-z]+)'
	# Checks if it's any number. Use this instead of making a very similar looking
	# pattern_one regex. This is to prevent the unknown_wires from having any numbers as keys.
	number = r'(\d+)'

	# Extract the values of the wires that have a value and put them into a dictionary. This means that for the first
	# run, it would only look for numbers that are assigned to a value. Such as 123 -> x
	# Key: x
	# Val: 123
	known_wires = {}
	# Unknown wires should be everything else that we don't know yet.
	unknown_wires = defaultdict(lambda: None)

	for command in instructions:
		match_assign = re.search(pattern_number, command)
		match_pone = re.search(pattern_one, command)
		match_ptwo = re.search(pattern_two, command)
		match_pthree = re.search(pattern_three, command)

		if match_assign:
			known_wires[match_assign.group(2)] = int(match_assign.group(1))
		elif match_pone:
			# prevent numbers from being added as a key into unknown_wires.
			if not re.search(number, match_pone.group(3)):
				unknown_wires[match_pone.group(3)]
			if not re.search(number, match_pone.group(1)):
				unknown_wires[match_pone.group(1)]
			unknown_wires[match_pone.group(4)]
		elif match_ptwo:
			unknown_wires[match_ptwo.group(1)]
			unknown_wires[match_ptwo.group(2)]
		elif match_pthree:
			unknown_wires[match_pthree.group(2)]
			unknown_wires[match_pthree.group(2)]

	# Remove any known wires from the unknown wire dictionary.
	for w in known_wires:
		del unknown_wires[w]


	# Keeps looping until all wires are known.
	# If a wire is assigned, then we know it's value. It'll then remove that wire from the unknown wires dictionary.
	# So once the dictionary is empty, we know that every wire has been found.
	while len(unknown_wires) > 0:
		for command in instructions:
			match_pone = re.search(pattern_one, command)
			match_ptwo = re.search(pattern_two, command)
			match_pthree = re.search(pattern_three, command)
			# If the wire to be assigned in already in known_wires, we can skip it entirely and move onto the next.
			wire_to_be_assigned = command.split("->")[1].strip()
			if wire_to_be_assigned in known_wires:
				continue

			# This match can have only wire names: ls AND lx -> x
			# or a number and a wire: 1 AND lx -> x
			# or another variant: lx AND 1 -> x
			# First, we check if the input is even in this format.
			if match_pone:
				# Checks which place the number is located, in the beginning or the middle.
				match_number_one = re.search(number, match_pone.group(1))
				match_number_two = re.search(number, match_pone.group(3))

				# checks if the input is all wires, or a wire and number.
				# Necessary as we need to make sure the bitwise operator is done using
				# only numbers.
				if match_pone.group(1) in known_wires and match_pone.group(3) in known_wires:
					known_wires[match_pone.group(4)] = perform_bitwise(known_wires[match_pone.group(1)], \
						match_pone.group(2), known_wires[match_pone.group(3)])
					del unknown_wires[match_pone.group(4)]

				elif match_number_one and match_pone.group(3) in known_wires:
					known_wires[match_pone.group(4)] = perform_bitwise(int(match_pone.group(1)), \
						match_pone.group(2), known_wires[match_pone.group(3)])
					del unknown_wires[match_pone.group(4)]
				
				elif match_number_two and match_pone.group(1) in known_wires:
					known_wires[match_pone.group(4)] = perform_bitwise(known_wires[match_pone.group(1)], \
						match_pone.group(2), int(match_pone.group(3)))
					del unknown_wires[match_pone.group(4)]
				
				elif match_number_one and match_number_two:
					known_wires[match_pone.group(4)] = perform_bitwise(int(match_pone.group(1)), \
						match_pone.group(2), int(match_pone.group(3)))
					del unknown_wires[match_pone.group(4)]

			# Input matches NOT w -> x
			# performs the NOT bitwise function and assigns it to the wire.
			elif match_ptwo and match_ptwo.group(1) in known_wires:
				# print("Match P2")
				known_wires[match_ptwo.group(2)] = ~ known_wires[match_ptwo.group(1)]
				del unknown_wires[match_ptwo.group(2)]
			elif match_pthree and match_pthree.group(1) in known_wires:
				# print("Match P3")
				known_wires[match_pthree.group(2)] = known_wires[match_pthree.group(1)]
				del unknown_wires[match_pthree.group(2)]
			
	return known_wires['a']


'''
 ----- Part 2 -----
It's literally the same thing, except you take the value for wire a and put it into wire b, reset all the wires
from before, and then get the new output of wire a.

What I'm going to do is copy the function for part 1 and make slight changes to it.
The only change is line 172, the passed parameters to the function.
The other change is line 201, don't override values in the known_wires.
'''

def part_two(instructions: list, known_wires = {}) -> int:
	# Expressions that look like: lf and lq -> ls
	pattern_one = r'([a-z]+|\d+) (AND|OR|RSHIFT|LSHIFT) ([a-z]+|\d+) -> ([a-z]+)'
	# Expressions that look like: NOT kt -> ku
	pattern_two = r'^NOT ([a-z]+) -> ([a-z]+)'
	# Expressions that look like: x -> y
	pattern_three = r'^([a-z]+) -> ([a-z]+)'
	# Expressions that look like: [0-9] -> y
	# Want this in order to put into the dictionary value.
	pattern_number = r'(^\d+) -> ([a-z]+)'
	# Checks if it's any number. Use this instead of making a very similar looking
	# pattern_one regex. This is to prevent the unknown_wires from having any numbers as keys.
	number = r'(\d+)'

	# Since this time we take a passed dictionary as a parameter, we can run it with just instructions,
	# and it'll act like part 1, but since we need to change the value of a certain wire, we can
	# pass it a dictionary of known wires, in this case, a -> b.

	# Unknown wires should be everything else that we don't know yet.
	unknown_wires = defaultdict(lambda: None)

	for command in instructions:
		match_assign = re.search(pattern_number, command)
		match_pone = re.search(pattern_one, command)
		match_ptwo = re.search(pattern_two, command)
		match_pthree = re.search(pattern_three, command)

		if match_assign:
			# ----- Changed from Part 1 -----
			# If the wire is already in the dictionary, don't override it.
			if match_assign.group(2) not in known_wires:
				known_wires[match_assign.group(2)] = int(match_assign.group(1))
		elif match_pone:
			# prevent numbers from being added as a key into unknown_wires.
			if not re.search(number, match_pone.group(3)):
				unknown_wires[match_pone.group(3)]
			if not re.search(number, match_pone.group(1)):
				unknown_wires[match_pone.group(1)]
			unknown_wires[match_pone.group(4)]
		elif match_ptwo:
			unknown_wires[match_ptwo.group(1)]
			unknown_wires[match_ptwo.group(2)]
		elif match_pthree:
			unknown_wires[match_pthree.group(2)]
			unknown_wires[match_pthree.group(2)]

	# Remove any known wires from the unknown wire dictionary.
	for w in known_wires:
		del unknown_wires[w]


	# Keeps looping until all wires are known.
	# If a wire is assigned, then we know it's value. It'll then remove that wire from the unknown wires dictionary.
	# So once the dictionary is empty, we know that every wire has been found.
	while len(unknown_wires) > 0:
		for command in instructions:
			match_pone = re.search(pattern_one, command)
			match_ptwo = re.search(pattern_two, command)
			match_pthree = re.search(pattern_three, command)
			# If the wire to be assigned in already in known_wires, we can skip it entirely and move onto the next.
			wire_to_be_assigned = command.split("->")[1].strip()
			if wire_to_be_assigned in known_wires:
				continue

			# This match can have only wire names: ls AND lx -> x
			# or a number and a wire: 1 AND lx -> x
			# or another variant: lx AND 1 -> x
			# First, we check if the input is even in this format.
			if match_pone:
				# Checks which place the number is located, in the beginning or the middle.
				match_number_one = re.search(number, match_pone.group(1))
				match_number_two = re.search(number, match_pone.group(3))

				# checks if the input is all wires, or a wire and number.
				# Necessary as we need to make sure the bitwise operator is done using
				# only numbers.
				if match_pone.group(1) in known_wires and match_pone.group(3) in known_wires:
					known_wires[match_pone.group(4)] = perform_bitwise(known_wires[match_pone.group(1)], \
						match_pone.group(2), known_wires[match_pone.group(3)])
					del unknown_wires[match_pone.group(4)]

				elif match_number_one and match_pone.group(3) in known_wires:
					known_wires[match_pone.group(4)] = perform_bitwise(int(match_pone.group(1)), \
						match_pone.group(2), known_wires[match_pone.group(3)])
					del unknown_wires[match_pone.group(4)]
				
				elif match_number_two and match_pone.group(1) in known_wires:
					known_wires[match_pone.group(4)] = perform_bitwise(known_wires[match_pone.group(1)], \
						match_pone.group(2), int(match_pone.group(3)))
					del unknown_wires[match_pone.group(4)]
				
				elif match_number_one and match_number_two:
					known_wires[match_pone.group(4)] = perform_bitwise(int(match_pone.group(1)), \
						match_pone.group(2), int(match_pone.group(3)))
					del unknown_wires[match_pone.group(4)]

			# Input matches NOT w -> x
			# performs the NOT bitwise function and assigns it to the wire.
			elif match_ptwo and match_ptwo.group(1) in known_wires:
				# print("Match P2")
				known_wires[match_ptwo.group(2)] = ~ known_wires[match_ptwo.group(1)]
				del unknown_wires[match_ptwo.group(2)]
			elif match_pthree and match_pthree.group(1) in known_wires:
				# print("Match P3")
				known_wires[match_pthree.group(2)] = known_wires[match_pthree.group(1)]
				del unknown_wires[match_pthree.group(2)]
			
	return known_wires['a']


wire_a = part_two(instructions)
known_wires = {'b': wire_a,}
print(part_two(instructions, known_wires))


class Test(unittest.TestCase):
	def test_part_one(self):
		self.assertEqual(part_one(['123 AND 456 -> a']), 72)
		self.assertEqual(part_one(["123 -> x", "456 -> y", "x AND y -> a"]), 72)
		# part_one(instructions)


if __name__ == "__main__":
	unittest.main()