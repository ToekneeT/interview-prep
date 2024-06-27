import unittest

#  ----- Part 1 -----
# The problem is getting the difference between the amount of characters in
# the actual string and the number of characters in the memory of the string.
# For example: "" -> 2 actual characters, 0 characters in memory.
# "abc" is 5 characters, but only 3 in memory.

# Each input looks like that.

# One simple way to get the actual character count is to just find the length
# of the string.

# To find the string size in memory, it's possible to just strip the string of
# the unnecessary characters, such as double quotes and backslashes.
# The issue is for inputs that look like this: "aaa\"aaa".
# The backslash doesn't count as a character, the double quote does.

# There's also the input "\x27" which is using hexadecimal to string, so the 
# character is actually just a single quote.
# Given that, any hexadecimal would only be one character long, and I assume that'd
# be until it reached the next backquote.
# So, this input: "\xa8br\x8bjr\""
# would only be 7 characters in memory long.
# Ignore the first and end double quotes leaving: \xa8br\x8bjr\"
# \x indicates hex to string, so a8 would be character: ", meaning only 1.
# Then we have br to count as 2 characters, so 3 in total.
# Then the pattern is repeated again, so now it's 4 characters long, leaving jr\"
# which jr is two characters, so 6 characters now. \" counts as one, so 7 characters in total.
# \" counts as one character as well as the \ indicates the next character to be a literal.

# Given that the last few AoCs have been only slight changes to the problems for part 2,
# I'm going to split the problem up even further. One function to parse through the input
# list and another to take in a string instead of the entire list.
# The function that finds the length of the string will probably be a return value of a
# tuple, one value being the actual length, the other being the memory length.


with open("aoc_2015_d8_input.txt") as file:
	strings: list[str] = [l.strip() for l in file]


# Removes the beginning and ending double quote from the equation.
def remove_beg_end(s: str) -> str:
	s_manip: str = s[1:]
	return s_manip[:len(s_manip) - 1]


# Originally, I was using regex to check the string for characters following \x because I didn't 
# read the part that only two characters followed the \x.
# So I thought that: \xa8br\x8bjr\"
# would go until it found another \, so a8br would the hex input.
# After realizing it was only two characters, I adjusted the regex to only take two characters after the
# \x and then slice the string. The error I made, though, was that I didn't make sure that the regex was only
# checking the first two characters of the string, it would instead check to find the first occurence of \x.
# Which was the bug that I was running into and made me think I was misunderstanding the problem.
# After finding that out, I realized I just didn't need to regex at all.
def count_characters(s: str) -> (int, int):
	actual_len: int = len(s)
	mem_len: int = 0
	s_manip: str = remove_beg_end(s)
	idx: int = 0
	# Traverses through the string character by character.
	# Checks for special inputs that involved \s.
	while idx < len(s_manip):
		# if the string has \x, the following two characters are hex values that return
		# one string, so 4 literal characters = 1 memory character.
		if s_manip[idx] == "\\" and s_manip[idx + 1] == "x":
			idx += 4
		# A character that has \followed by another character is just a literal of that,
		# so we only need to count it as one character in memory.
		elif s_manip[idx] == "\\":# and idx != len(s_manip) - 1:
			idx += 2
		else:
			idx += 1
		mem_len += 1

	return (actual_len, mem_len)


def diff_between(values: (int, int)) -> int:
	return values[0] - values[1]


def part_one(strings: list[str]) -> int:
	string_diff_sum: int = 0
	for s in strings:
		string_diff_sum += diff_between(count_characters(s))

	return string_diff_sum


#  ----- Part 2 -----
# Now it's the opposite, we're going to make every memory code into a literal.
# So: "" turns into "\"\"", meaning it'd be 6 characters long.
# Seems that instead of actually encoding it to be longer, we can just add to it.
# So we can parse the string without removing the beginning and the ending.
# If it finds a double quote, we add 3 instead of 1. 3 because the original double quote,
# then the new \, and the other added double quote.
# If we find a \x, we add 3 as well, moving past the x.
# If we have a \", that adds 4 to the total. Since we'd add a new \ for each character.
# If we find an \\, that would add 4 total as well. Since we'd add a new \ for each backslash.

# Had to whip out the calculator to do the math for the inputs to understand how much it was adding.


def count_characters_p2(s: str) -> (int, int):
	actual_len: int = len(s)
	increased_len: int = 0
	idx: int = 0
	while idx < len(s):
		# idx changes depending on the type of input.
		# If there's a \, we skip two characters as
		# we want to skip the character ahead of it.
		# otherwise, we just move up one.
		if s[idx] == '"':
			idx += 1
			increased_len += 3
		elif s[idx] == "\\" and s[idx + 1] == "x":
			idx += 2
			increased_len += 3
		elif s[idx] == "\\" and s[idx + 1] == '"':
			idx += 2
			increased_len += 4
		elif s[idx] == "\\" and s[idx + 1] == "\\":
			idx += 2
			increased_len += 4
		else:
			idx += 1
			increased_len += 1

	return (increased_len, actual_len)


def part_two(strings: list[str]) -> int:
	string_diff_sum: int = 0
	for s in strings:
		string_diff_sum += diff_between(count_characters_p2(s))

	return string_diff_sum


# Time Complexity: O(n + x) where n is the length of the input, in this case a list of strings.
# The length of the individual strings, x,  are varying lengths, while unlikely, it is possible the string
# could be longer than the actual length of the input list.

class Test(unittest.TestCase):
	def test_part_one(self):
		self.assertEqual(remove_beg_end("\"abc\""), "abc")
		self.assertEqual(count_characters("\"abc\""), (5, 3))
		self.assertEqual(count_characters('"\\""'), (4, 1))
		self.assertEqual(count_characters("\"x\""), (3, 1))
		self.assertEqual(count_characters('""'), (2, 0))
		self.assertEqual(count_characters('"aaa\\"aaa"'), (10, 7))
		self.assertEqual(diff_between((4, 2)), 2)
		self.assertEqual(part_one(["\"abc\"", "\"nq\""]), 4)
	
	def test_part_two(self):
		self.assertEqual(count_characters_p2('""'), (6, 2))
		self.assertEqual(count_characters_p2('"abc"'), (9, 5))
		self.assertEqual(count_characters_p2('"\\x27"'), (11, 6))
		self.assertEqual(count_characters_p2('"aaa\\"aaa"'), (16, 10))
		self.assertEqual(count_characters_p2('\\\\'), (4, 2))

if __name__ == "__main__":
	unittest.main()