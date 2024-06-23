import unittest
import copy
'''
 ----- Part 1 -----
Given a 8 character string, provide the next valid string from it.
The strings cannot have the letters i, o, or l.
Has to have two different non-overlapping pairs of letters, such as
aa, bb, or zz.
Must have one increasing straight of at least three letters, such as
abc, bcd, cde,...xyz.
Next valid string after ghijklmn is ghjaabcc as i and l are not valid letters.


To start, would probably interate through the entire string and get each letter as a char.
Have either a dict or a list of the character values that aren't allowed, such as i, o, and l.
And increment the character by one unless it'd make the character equal to one of invalid characters.
Then to check the other conditions, if the character isn't equal to the next character, then we'll skip it since
it's invalid. Also check that there are three characters that are increments of each other.

'''

with open("aoc_2015_d11_input.txt") as file:
	curr_pass: str = file.readline()


invalid_char: dict = {
	'i': ord('i'),
	'o': ord('o'),
	'l': ord('l'),
	}


# Increases the character once alphabetically by using unicode decimal values.
# If it tries to increase the letter z, it'll go back to the letter a.
def inc_char(c: str) -> str:
	next_char = ord(c) + 1
	if next_char == 123:
		return chr(97)
	return chr(next_char)


# Checks if the passed password is valid by the given rules.
def is_valid_pass(psw: list) -> bool:
	# Checks if the string contain any invalid letters.
	for i in range(len(psw)):
		if psw[i] in invalid_char:
			return False

	# Checks if there's a double letter anywhere in the string by checking if it's equal to the next letter.
	double_letter_count = 0
	i = 0
	while i < len(psw) - 1:
		if psw[i] == psw[i+1]:
			double_letter_count += 1
			# Skip past the letter we just checked if it's a valid double letter.
			# That way we can skip any triples such as: 'aaa'
			i += 1
		i += 1


	double_letter: bool = double_letter_count >= 2

	if not double_letter:
		return False

	# Checks if there are any triple alphabetical sequence.
	increasing_straight: bool = False
	for i in range(len(psw)-2):
		if ord(psw[i]) == ord(psw[i+1]) - 1 and ord(psw[i+1]) == ord(psw[i+2]) - 1:
			increasing_straight = True

	return increasing_straight


# Turns a list into a string by concatenation.
def list_to_str(l: list) -> str:
	s = ""
	for c in l:
		s += c

	return s


# At some point I realized that recursion might be easier for this.
# The reason is because of the deep copy of the list.
# I think if I used recursion, I wouldn't need to do a deep copy and could compare
# previous password with the new one.
def next_pass(curr_pass: str) -> str:
	valid_pass: bool = False
	# Turns the new pass into a list as a string isn't mutable.
	new_pass: list = [""] * len(curr_pass)
	for i in range(len(curr_pass)):
		new_pass[i] = curr_pass[i]

	comparision_pass: list = copy.deepcopy(new_pass)

	while not valid_pass:
		comparision_pass = copy.deepcopy(new_pass)
		for i in range(len(comparision_pass)):
			if comparision_pass[i] in invalid_char:
				new_pass[i] = inc_char(comparision_pass[i])
				for j in range(i + 1, len(comparision_pass)):
					new_pass[j] = 'a'
				comparision_pass = copy.deepcopy(new_pass)

			# Always increase the last character of the password.
			if i == len(comparision_pass) - 1:
				new_pass[i] = inc_char(comparision_pass[i])
				# If the new character is an 'a', then that means it was increased from z.
				# So, the previous character needs to be increased.
				# This solution is really bad, it was very annoying to wrap my head around when coming up with it,
				# and I already didn't like my solution to the rest of the code, so I'm going to re-do it, most likely.
				inc_z: int = 0
				while new_pass[i+inc_z] == 'a':
					new_pass[i+inc_z-1] = inc_char(new_pass[i+inc_z-1])
					inc_z -= 1

		valid_pass = is_valid_pass(new_pass)
	
	return list_to_str(new_pass)


# I really hate my solution, and I'm going to fix it.

# ----- Stuff below is the new solution -----

# Recursively increases the last letter of a given string and does rollover if the last letter was a z.
def increase_last_char(s: str) -> str:
	if len(s) == 0:
		return ''
	elif s[-1] == 'z':
		# If the last character is z, rollover to a and recursively handle previous characters.
		return increase_last_char(s[:-1]) + 'a'
	# Increment the last character alphabetically
	new_last_char: str = chr(ord(s[-1]) + 1)
	return s[:-1] + new_last_char


def next_valid_pass(curr_pass: str) -> str:
	# Base case, if the password is valid, we can stop.
	if is_valid_pass(curr_pass):
		return curr_pass

	new_pass = []
	for c in curr_pass:
		new_pass.append(c)

	for i in range(len(new_pass)):
		if new_pass[i] in invalid_char:
			new_pass[i] = increase_last_char(new_pass[i])
			for j in range(i + 1, len(new_pass)):
				new_pass[j] = 'a'
			next_pass: str = list_to_str(new_pass)
			return next_valid_pass(next_pass)

		if i == len(new_pass) - 1:
			next_pass: str = list_to_str(new_pass)
			return next_valid_pass(increase_last_char(next_pass))


# Converts a string to a list.
# This is needed as next_pass_two uses lists to assign values, which can't be done with strings.
def str_to_list(s: str) -> list:
	s_list = []
	for c in s:
		s_list.append(c)

	return s_list


def next_pass_two(curr_pass: str) -> str:
	valid_pass: bool = False
	# Turns the new pass into a list as a string isn't mutable.
	new_pass: list = str_to_list(curr_pass)

	while not valid_pass:
		for i in range(len(new_pass)):
			if new_pass[i] in invalid_char:
				new_pass[i] = increase_last_char(new_pass[i])
				for j in range(i + 1, len(new_pass)):
					new_pass[j] = 'a'

			# Always increase the last character of the password.
			if i == len(new_pass) - 1:
				next_pass: str = list_to_str(new_pass)
				next_pass = increase_last_char(next_pass)
				new_pass = str_to_list(next_pass)

		valid_pass = is_valid_pass(new_pass)
	
	return list_to_str(new_pass)


'''
 ----- Part 2 -----
It's just running it again on the password from part 1. No changes needed.
'''
# print(next_valid_pass(curr_pass))

class Test(unittest.TestCase):
	def test_is_valid_pass(self):
		self.assertFalse(is_valid_pass("ghijklmn"))
		self.assertTrue(is_valid_pass("ghjaabcc"))

	def test_inc_char(self):
		self.assertEqual(inc_char("a"), "b")
		self.assertEqual(inc_char("z"), "a")

	def test_next_pass(self):
		self.assertEqual(next_pass("ghijklmn"), "ghjaabcc")

	def test_increase_last_char(self):
		self.assertEqual(increase_last_char("abc"), "abd")
		self.assertEqual(increase_last_char("abz"), "aca")
		self.assertEqual(increase_last_char("azz"), "baa")
		self.assertEqual(increase_last_char("a"), "b")
		self.assertEqual(increase_last_char("z"), "a")

	def test_next_valid_pass(self):
		self.assertEqual(next_valid_pass("ghijklmn"), "ghjaabcc")

	def test_next_pass_two(self):
		self.assertEqual(next_pass_two("ghijklmn"), "ghjaabcc")


if __name__ == '__main__':
	unittest.main()